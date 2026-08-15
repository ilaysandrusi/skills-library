# דוח יומי במייל

אחרי כל ריצה הסוכן מעדכן את `reports/latest.html` ודוחף ל-GitHub. GitHub Actions שולח את הקובץ ל-Gmail.

## הגדרה חד-פעמית (כשתי דקות)

1. סיסמת אפליקציה ל-Gmail (לא סיסמת החשבון הרגילה):
   - [הפעל אימות דו-שלבי](https://myaccount.google.com/signinoptions/two-step-verification) אם עדיין לא פעיל.
   - צור סיסמת אפליקציה בשם `Skills Library`: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. הוסף סודות לריפו:
   [Settings → Secrets and variables → Actions](https://github.com/ilaysandrusi/skills-library/settings/secrets/actions)
   - `SMTP_USER` = `ilaysan159@gmail.com`
   - `SMTP_PASSWORD` = סיסמת 16 התווים שגוגל נתנה
   - אופציונלי: `MAIL_TO` (ברירת מחדל: אותה כתובת)
3. שליחה ראשונה ידנית:
   [Actions → Email daily skills report → Run workflow](https://github.com/ilaysandrusi/skills-library/actions/workflows/email-daily-report.yml)

מהיום הבא המייל יישלח לבד בכל פעם ש-`reports/latest.html` מתעדכן ב-push.
