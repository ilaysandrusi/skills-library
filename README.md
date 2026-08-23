# ספריית הסקילים שלי

פה מרוכזים כל הסקילים ללמידה ולעיון. הפרויקט של האתר (`ilay_sandrusi_website`) מחזיק רק את מה שצריך לאתר.

**סה״כ סקילים:** 6091

## איך ללמוד

1. פתח קטגוריה למטה.
2. קרא את טבלת השמות ב-README של הקטגוריה.
3. היכנס לתיקיית הסקיל ופתח את `SKILL.md`.

לחיפוש סקיל לפי שם או נושא: `catalog.json` מכיל את האינדקס המלא, או חפש עם `rg -i "מילת-מפתח" catalog.json`.

## לא רק סקילים

חלק מהמקורות מספקים גם ארטיפקטים נלווים לאותו פרויקט. הם לא הומרו לסקילים, ומאוחסנים
בשני מקומות לפי בעלות:

**בתוך הסקיל.** אם מבנה מעלה הזרם מוכיח שהארטיפקט שייך לסקיל אחד ספציפי, הוא יושב
בתיקיית הסקיל עצמו, כך שהסקיל הוא חבילה עצמאית שאפשר להעתיק כמו שהיא:

```
<category>/<skill>/
├── SKILL.md          ← הסקיל
├── SOURCE.md         ← ריפו מקור, commit, רישיון, והוכחת הבעלות
├── agents/ commands/ rules/ hooks/
└── references/ scripts/ assets/
```

אם ריפו המקור מפרסם סקיל אחד ומכיל גם runtime, קונפיג, בדיקות, workflows או docs שמשרתים
את אותו סקיל, גם הם נשמרים בתוך תיקיית הסקיל. המטרה היא שהתקנת סקיל מתוך הספרייה לא תביא
רק הוראות, אלא גם את קבצי ההפעלה והתפעול שעוזרים להריץ אותו בצורה נכונה.

**משותף.** ארטיפקט שברמת הריפו ומשרת כמה סקילים במקביל נשאר בעץ המשותף:

| תיקייה | קבצים | מה זה |
|---|---|---|
| [`agents/`](./agents/) | 374 | סוכני משנה שהסוכן הראשי מאציל להם משימות |
| [`commands/`](./commands/) | 408 | פקודות סלאש שמופעלות במפורש |
| [`rules/`](./rules/) | 174 | חוקים תמידיים לשפה, פריימוורק או סטייל |
| [`hooks/`](./hooks/) | 99 | הוקים של זמן ריצה (`hooks.json` וסקריפטים) |

הסבר מלא, כולל למה משהו נשאר משותף: [`ARTIFACTS.md`](./ARTIFACTS.md).
מדיניות ייבוא ושמירת חבילות מלאות: [`ARCHIVE_POLICY.md`](./ARCHIVE_POLICY.md).
שיוך מקור לכל סקיל: [`SOURCES.json`](./SOURCES.json).

## קטגוריות

| קטגוריה | סקילים | תיאור |
|---|---|---|
| [כתיבה וניקוי טקסט](./01-copy-writing/) | 100 | עצירת סלופ AI, קופי, הנחיות כתיבה |
| [עיצוב וממשק](./02-design-ui/) | 122 | UI/UX, פרונט, נגישות, גלילה |
| [שיווק ותוכן](./03-marketing/) | 536 | חבילת Corey Haines וסקילים שיווקיים |
| [Remotion (וידאו מקוד)](./04-remotion/) | 12 | יצירת וידאו עם React / Remotion |
| [פיתוח ודיבאג](./05-development/) | 565 | Superpowers, בדיקות, תוכניות עבודה |
| [מסמכים](./06-documents/) | 40 | PDF, Word, PowerPoint, Excel |
| [Supabase / Postgres](./07-supabase/) | 4 | עבודה עם מסדי נתונים של Supabase |
| [Context Engineering](./08-context-engineering/) | 171 | ניהול קונטקסט, סוכני משנה, חשיבה |
| [כלי Anthropic נוספים](./09-anthropic-tools/) | 5 | יצירת סקילים, תבניות, בדיקות וכו׳ |
| [Hyper — פלטפורמות שיווק ומודעות (MCP)](./10-hyperfx-marketing/) | 30 | חבילת hyperfx-ai: פלטפורמות מודעות (Google/Meta/TikTok ועוד), סושיאל, SEO ותפעול — רץ מעל Hyper MCP |
| [ניהול מוצר](./11-product-management/) | 149 | חבילות Dean Peters ו-Pawel Huryn: אסטרטגיה, דיסקברי, PRD, תעדוף, מטריקות ו-GTM |
| [אבטחה וביקורת קוד](./12-security/) | 157 | Trail of Bits, Snyk, OpenAI ו-Sentry: סקירות אבטחה, ניתוח סטטי, Semgrep/CodeQL ומודלי איומים |
| [ענן ופריסה](./13-cloud-deploy/) | 171 | Cloudflare, Netlify, Firebase, HashiCorp, AWS ו-Next.js: פריסות, תשתיות ו-DevOps |
| [בדיקות ואוטומציה](./14-testing-qa/) | 204 | LambdaTest, Cypress, Playwright, Browserbase ואוטומציית דפדפן: בדיקות, נגישות ו-CI/CD |
| [אינטגרציות ושירותים](./15-integrations/) | 257 | Stripe, Better Auth, Sentry, Resend, Notion, Zapier, n8n, WordPress, Google Workspace ועוד |
| [AI APIs ומדיה](./16-ai-apis-media/) | 242 | OpenAI, Gemini, Hugging Face, Replicate, fal.ai, MiniMax: תמונות, וידאו, קול ומוזיקה |
| [חבילת סייבר ענקית](./17-cybersecurity-pack/) | 821 | אנציקלופדיית סקילי סייבר (800+): פורנזיקה, תגובה לאירועים, מודיעין איומים, פנטסטינג והקשחה |
| [פיננסים וחשבונאות](./18-finance-accounting/) | 791 | openaccountants (780+), CFO, ניתוח מניות ודוחות: הנהלת חשבונות, מס, ביקורת ותכנון פיננסי |
| [מכירות, GTM וסטארטאפ](./19-sales-gtm-startup/) | 298 | Infrasity dev-GTM, GTM co-founder, סקילים למייסדים ולסטארטאפים בשלב מוקדם |
| [NVIDIA ו-CUDA](./20-nvidia-cuda/) | 341 | הסקילים הרשמיים של NVIDIA: CUDA, GPU, ביצועים, רשתות עצביות ותשתית AI |
| [Goose Agent](./21-goose-agent/) | 263 | חבילת הסקילים של gooseworks: 260+ סקילים לסוכן Goose של Block |
| [Microsoft](./23-microsoft/) | 187 | הסקילים הרשמיים של מיקרוסופט: Azure, .NET, TypeSpec, Playwright, GitHub ועוד |
| [דאטה ובסיסי נתונים](./25-data-databases/) | 112 | MongoDB, Redis, Qdrant, DuckDB, ClickHouse, Neon, Tinybird, Milvus ו-VideoDB |
| [מובייל ו-Apple](./26-mobile-apple/) | 136 | Flutter, Expo, React Native, Swift/SwiftUI, iOS, App Store Connect ו-HIG |
| [Web3 וקריפטו](./27-web3-crypto/) | 47 | Binance, Coinbase, Helius (Solana): ארנקים, מסחר ופיתוח בלוקצ'יין |
| [קריירה, חינוך ובריאות](./28-career-education-health/) | 45 | קורות חיים, ניהול קריירה, חונכות לימודית ובריאות אישית |
| [ECC (Everything Claude Code)](./29-ecc/) | 285 | חבילת affaan-m/ECC — 285 סקילים; ה-agents/rules/hooks/commands שלה בתיקיות הארטיפקטים |
| [אחר](./99-other/) | 0 | סקילים שלא סווגו לקטגוריה ברורה |

## כלי תחזוקה

בדיקת עקביות בין `catalog.json`, קבצי README, שיוך מקורות וקבצי `SKILL.md` בפועל:

```bash
node tools/validate-catalog.mjs
node tools/validate-catalog.mjs --strict-source-files
```

חיפוש והתקנת סקיל מתוך הספרייה אל תיקיית ה-skills האישית של Codex:

```bash
node tools/install-skill.mjs --list outreach
node tools/install-skill.mjs 15-integrations/agent-reach
```

רישום סקילים חדשים שהועתקו לספרייה בכל האינדקסים (`catalog.json`, README של הקטגוריה,
README ראשי ו-`SOURCES.json`). הקובץ מקבל רשימת `{"category","slug"}` ומוסיף רק את מה
שחסר — שורות קיימות מועתקות כמו שהן, כי חלק מהתיאורים הישנים לא ניתנים לשחזור מה-frontmatter:

```bash
python3 tools/index-skills.py new-skills.json \
  --source owner/repo --note "daily maintenance" --check
```

הוצאת סקילים משירות — מוחקת את התיקייה ומסירה אותה מאותם אינדקסים. גם כאן שורות שנשארות
מועתקות כמו שהן. הסרה של יותר מ-10 סקילים בריצה אחת חסומה בכוונה ודורשת
`--allow-mass-removal`, כדי שניקוי המוני לא יקרה בטעות:

```bash
python3 tools/remove-skills.py retire.json \
  --reason "test fixtures, not real skills" --check
```

בדיקה מול המקור: משווה כל קובץ בכל סקיל של ריפו מסוים ל-upstream לפי git blob SHA. התאמה
מלאה אומרת שהעותק המקומי הוא בדיוק אותו commit, ולכן אפשר לרשום אותו כ-baseline אמין. מצב
הבדיקות האחרון, כולל commit מאומת לכל מקור ותור לבדיקה ידנית, נשמר ב-
[`UPDATE_CHECKS.json`](./UPDATE_CHECKS.json):

```bash
python3 tools/check-upstream.py anthropics/skills
python3 tools/check-upstream.py trailofbits/skills --json
```

כשתיקיית ה-upstream קיימת אבל אף קובץ לא מתאים, זה יכול להיות שכתוב מלא של הסקיל (עדכון
שכדאי לקחת) או סקיל אחר לגמרי עם אותו שם (עדכון שימחק את הסקיל המקומי). blob SHA לא מבדיל
ביניהם, ולכן `--probe-frontmatter` קורא את ה-`SKILL.md` במעלה הזרם ומשווה את `name` ו-`description`
לשלנו. זהות מלאה היא עדות חזקה שזה אותו סקיל; `name-differs` מוכיח התנגשות שמות:

```bash
python3 tools/check-upstream.py firecrawl/skills --probe-frontmatter
python3 tools/check-upstream.py --rotate 20 --record --probe-frontmatter
```
