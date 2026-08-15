#!/usr/bin/env python3
"""Send reports/latest.html via Gmail SMTP.

Required environment:
  SMTP_USER      Gmail address used to send
  SMTP_PASSWORD  Gmail App Password (16 characters), not the normal password

Optional:
  MAIL_TO        Recipient (default: ilaysan159@gmail.com)
  MAIL_FROM      From header (default: SMTP_USER)
  REPORT_HTML    Path to HTML body (default: reports/latest.html)
"""

from __future__ import annotations

import os
import smtplib
import sys
from email.message import EmailMessage
from html.parser import HTMLParser
from pathlib import Path


DEFAULT_TO = "ilaysan159@gmail.com"
DEFAULT_HTML = Path("reports/latest.html")


class _TitleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._in_title = False
        self.title = ""

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag.lower() == "title":
            self._in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data


def subject_from_html(html: str) -> str:
    parser = _TitleParser()
    parser.feed(html)
    title = " ".join(parser.title.split())
    return title or "Skills Library — דוח יומי"


def main() -> int:
    user = (os.environ.get("SMTP_USER") or "").strip()
    password = (os.environ.get("SMTP_PASSWORD") or "").strip()
    mail_to = (os.environ.get("MAIL_TO") or DEFAULT_TO).strip()
    mail_from = (os.environ.get("MAIL_FROM") or user).strip()
    html_path = Path(os.environ.get("REPORT_HTML") or DEFAULT_HTML)

    if not user or not password:
        print(
            "SMTP_USER / SMTP_PASSWORD are not set. "
            "Add GitHub Actions secrets, then re-run the workflow. Skipping send."
        )
        return 0

    if not html_path.is_file():
        print(f"Report file not found: {html_path}", file=sys.stderr)
        return 1

    html = html_path.read_text(encoding="utf-8")
    subject = subject_from_html(html)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = mail_from
    msg["To"] = mail_to
    msg.set_content(
        "הדוח היומי מצורף כ-HTML. אם אינך רואה עיצוב, פתח את ההודעה בדפדפן."
    )
    msg.add_alternative(html, subtype="html")

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(msg)

    print(f"Sent daily report to {mail_to}: {subject}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
