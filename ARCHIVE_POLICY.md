# מדיניות ארכיון סקילים

הספרייה הזאת היא **ארכיון הפעלה** ל-Agent Skills שמצאת, לא רק אוסף קבצי
`SKILL.md`. כשמייבאים skill, המטרה היא לשמר מספיק הקשר כדי להבין, להתקין,
להריץ, לבדוק ולעדכן אותו בעתיד.

## עקרון בסיס

כל skill צריך להישמר כחבילה עצמאית ככל שזה נכון לפי מבנה המקור:

```text
<category>/<skill>/
├── SKILL.md
├── SOURCE.md
├── references/
├── scripts/
├── assets/
├── agents/
├── commands/
├── rules/
├── hooks/
├── config/
├── docs/
├── tests/
└── runtime files such as pyproject.toml, package.json, .env.example, workflows
```

לא כל תיקייה מהריפו המקורי נכנסת אוטומטית לתוך כל skill. הקובע הוא בעלות:
האם הקובץ משרת skill מסוים, כמה skills, או את כל הריפו המקורי.

## מה מייבאים

ייבא לתוך תיקיית ה-skill כל קובץ שמשרת את ההפעלה או התחזוקה שלו:

- `SKILL.md` וקבצי skill חלופיים כמו `SKILL_en.md`
- `references/`, `templates/`, `assets/`, `examples/`
- `scripts/`, `bin/`, `src/`, `lib/`, package/runtime code
- `agents/`, `commands/`, `rules/`, `hooks/` כאשר הם שייכים ל-skill הזה
- `config/`, `.env.example`, lock/config files, `pyproject.toml`, `package.json`
- `docs/`, `README.md`, `CHANGELOG.md`, `SECURITY.md`, `CONTRIBUTING.md`
- `tests/`, fixtures, CI workflows שמראים איך בודקים או מריצים
- רישיונות, notices, attribution files

אל תייבא secrets, caches, build outputs זמניים, `node_modules`, virtualenvs, או
קבצי מצב מקומיים שלא שייכים ל-upstream.

## כללי בעלות

העבר קובץ לתוך תיקיית skill רק כשיש ראיה ברורה שהוא שייך אליו:

1. ריפו המקור מפרסם skill אחד בדיוק, ולכן קבצי הריפו משרתים אותו.
2. תיקיית upstream של plugin או package מכילה skill אחד בדיוק ולידו artifacts.
3. הקובץ נמצא בתוך תיקיית ה-skill במקור.
4. קובץ README/config/test מזכיר במפורש את ה-skill או את CLI/runtime שלו.
5. כמה וריאנטים upstream אוחדו כאן ל-skill מקומי אחד, וה-artifacts שייכים למשפחה המאוחדת.

אם artifact משרת כמה skills, השאר אותו בעץ משותף תחת `agents/`, `commands/`,
`rules/` או `hooks/`, עם `SOURCE.md` שמסביר את המקור והבעלות.

אם אין ראיה, אל תנחש. עדיף להשאיר artifact משותף ומתועד מאשר להכניס אותו
ל-skill הלא נכון.

## SOURCE.md

כל skill חדש או self-contained חייב לקבל `SOURCE.md`.

`SOURCE.md` צריך לכלול:

- repository upstream
- URL
- imported commit או tag
- local path
- license, אם ידוע
- מה יובא
- למה הקבצים התומכים שייכים ל-skill הזה

דוגמה קצרה:

```md
# Source

- Repository: `owner/repo`
- URL: https://github.com/owner/repo
- Imported commit: `abc123`
- Local skill path: `15-integrations/example-skill`
- License: MIT

## Ownership

This upstream repository publishes one skill and the adjacent runtime, docs,
tests, workflows, and config files are used to run that skill.
```

## תהליך ייבוא

1. זהה את upstream: repo, branch/tag/commit, license.
2. בדוק אם זה repo של skill יחיד או חבילה עם כמה skills.
3. העתק את ה-skill ואת כל הקבצים התומכים שבבעלותו.
4. מקם artifacts משותפים בעץ המשותף רק אם הם באמת משותפים.
5. הוסף או עדכן `SOURCE.md`.
6. עדכן `catalog.json`, `SOURCES.json` ו-README של הקטגוריה.
7. הרץ `node tools/validate-catalog.mjs`.
8. בדוק התקנה עם `node tools/install-skill.mjs <category>/<skill> --dest <temp-dir> --force`.
9. בצע commit עם הודעה שמתארת את ה-skill ואת scope הייבוא.

## Hooks

`hooks/` הם קוד שרץ אוטומטית באירועים של סוכן קוד. הם חשובים, אבל הם גם
החלק הכי רגיש בארכיון.

לפני שמחברים hook לסביבת עבודה אמיתית:

- קרא את הקובץ.
- בדוק אם הוא מוריד dependencies, משנה PATH, מתקין packages, או כותב לתיקיית הבית.
- ודא שהוא שייך ל-skill או ל-plugin הנכון.
- העדף מצב read-only או dry-run אם קיים.

שמירה בארכיון אינה אומרת שה-hook מופעל אוטומטית.

## התקנה מתוך הארכיון

התקנה צריכה להעתיק את כל תיקיית ה-skill, לא רק את `SKILL.md`:

```bash
node tools/install-skill.mjs 15-integrations/agent-reach
```

כך נשמרים גם references, scripts, config, tests, docs, workflows וקבצי runtime
שנמצאים בתוך תיקיית ה-skill.

## מצב ידוע

הספרייה כוללת גם imports היסטוריים שלא כולם עומדים במדיניות החדשה. זה תקין
בינתיים. המדיניות חלה על imports חדשים, ועל תיקוני עומק כשנוגעים ב-skill קיים.

כדי לראות פערים:

```bash
node tools/validate-catalog.mjs
```

כדי להפוך חוסר `SOURCE.md` לכשל מפורש, למשל אחרי השלמת תיקון רוחבי:

```bash
node tools/validate-catalog.mjs --strict-source-files
```
