# ספריית הסקילים שלי

פה מרוכזים כל הסקילים ללמידה ולעיון. הפרויקט של האתר (`ilay_sandrusi_website`) מחזיק רק את מה שצריך לאתר.

**סה״כ סקילים:** 6522

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

**משותף.** ארטיפקט שברמת הריפו ומשרת כמה סקילים במקביל נשאר בעץ המשותף:

| תיקייה | קבצים | מה זה |
|---|---|---|
| [`agents/`](./agents/) | 224 | סוכני משנה שהסוכן הראשי מאציל להם משימות |
| [`commands/`](./commands/) | 303 | פקודות סלאש שמופעלות במפורש |
| [`rules/`](./rules/) | 163 | חוקים תמידיים לשפה, פריימוורק או סטייל |
| [`hooks/`](./hooks/) | 89 | הוקים של זמן ריצה (`hooks.json` וסקריפטים) |
| [`references/`](./references/) | 377 | עצי דוקומנטציה שהסקיל קורא בזמן עבודה |
| [`scripts/`](./scripts/) | 264 | סקריפטים שהסקיל מריץ |
| [`tools/`](./tools/) | 109 | רישומי כלים ומסמכי אינטגרציה |

הסבר מלא, כולל למה משהו נשאר משותף: [`ARTIFACTS.md`](./ARTIFACTS.md).
שיוך מקור לכל סקיל: [`SOURCES.json`](./SOURCES.json).

## קטגוריות

| קטגוריה | סקילים | תיאור |
|---|---|---|
| [כתיבה וניקוי טקסט](./01-copy-writing/) | 99 | עצירת סלופ AI, קופי, הנחיות כתיבה |
| [עיצוב וממשק](./02-design-ui/) | 109 | UI/UX, פרונט, נגישות, גלילה |
| [שיווק ותוכן](./03-marketing/) | 537 | חבילת Corey Haines וסקילים שיווקיים |
| [Remotion (וידאו מקוד)](./04-remotion/) | 12 | יצירת וידאו עם React / Remotion |
| [פיתוח ודיבאג](./05-development/) | 432 | Superpowers, בדיקות, תוכניות עבודה |
| [מסמכים](./06-documents/) | 34 | PDF, Word, PowerPoint, Excel |
| [Supabase / Postgres](./07-supabase/) | 2 | עבודה עם מסדי נתונים של Supabase |
| [Context Engineering](./08-context-engineering/) | 156 | ניהול קונטקסט, סוכני משנה, חשיבה |
| [כלי Anthropic נוספים](./09-anthropic-tools/) | 4 | יצירת סקילים, תבניות, בדיקות וכו׳ |
| [Hyper — פלטפורמות שיווק ומודעות (MCP)](./10-hyperfx-marketing/) | 30 | חבילת hyperfx-ai: פלטפורמות מודעות (Google/Meta/TikTok ועוד), סושיאל, SEO ותפעול — רץ מעל Hyper MCP |
| [ניהול מוצר](./11-product-management/) | 146 | חבילות Dean Peters ו-Pawel Huryn: אסטרטגיה, דיסקברי, PRD, תעדוף, מטריקות ו-GTM |
| [אבטחה וביקורת קוד](./12-security/) | 145 | Trail of Bits, Snyk, OpenAI ו-Sentry: סקירות אבטחה, ניתוח סטטי, Semgrep/CodeQL ומודלי איומים |
| [ענן ופריסה](./13-cloud-deploy/) | 97 | Cloudflare, Netlify, Firebase, HashiCorp, AWS ו-Next.js: פריסות, תשתיות ו-DevOps |
| [בדיקות ואוטומציה](./14-testing-qa/) | 197 | LambdaTest, Cypress, Playwright, Browserbase ואוטומציית דפדפן: בדיקות, נגישות ו-CI/CD |
| [אינטגרציות ושירותים](./15-integrations/) | 251 | Stripe, Better Auth, Sentry, Resend, Notion, Zapier, n8n, WordPress, Google Workspace ועוד |
| [AI APIs ומדיה](./16-ai-apis-media/) | 220 | OpenAI, Gemini, Hugging Face, Replicate, fal.ai, MiniMax: תמונות, וידאו, קול ומוזיקה |
| [חבילת סייבר ענקית](./17-cybersecurity-pack/) | 817 | אנציקלופדיית סקילי סייבר (800+): פורנזיקה, תגובה לאירועים, מודיעין איומים, פנטסטינג והקשחה |
| [פיננסים וחשבונאות](./18-finance-accounting/) | 788 | openaccountants (780+), CFO, ניתוח מניות ודוחות: הנהלת חשבונות, מס, ביקורת ותכנון פיננסי |
| [מכירות, GTM וסטארטאפ](./19-sales-gtm-startup/) | 293 | Infrasity dev-GTM, GTM co-founder, סקילים למייסדים ולסטארטאפים בשלב מוקדם |
| [NVIDIA ו-CUDA](./20-nvidia-cuda/) | 338 | הסקילים הרשמיים של NVIDIA: CUDA, GPU, ביצועים, רשתות עצביות ותשתית AI |
| [Goose Agent](./21-goose-agent/) | 263 | חבילת הסקילים של gooseworks: 260+ סקילים לסוכן Goose של Block |
| [משפטים](./22-legal/) | 238 | awesome-legal-skills: חוזים, רגולציה, ליטיגציה, קניין רוחני ותאימות |
| [Microsoft](./23-microsoft/) | 186 | הסקילים הרשמיים של מיקרוסופט: Azure, .NET, TypeSpec, Playwright, GitHub ועוד |
| [מדע ומחקר](./24-science-research/) | 542 | K-Dense scientific, AI-research, MedSci (מחקר רפואי קליני), סימולציות חומרים, הנדסה ומחקר אוטומטי |
| [דאטה ובסיסי נתונים](./25-data-databases/) | 78 | MongoDB, Redis, Qdrant, DuckDB, ClickHouse, Neon, Tinybird, Milvus ו-VideoDB |
| [מובייל ו-Apple](./26-mobile-apple/) | 135 | Flutter, Expo, React Native, Swift/SwiftUI, iOS, App Store Connect ו-HIG |
| [Web3 וקריפטו](./27-web3-crypto/) | 43 | Binance, Coinbase, Helius (Solana): ארנקים, מסחר ופיתוח בלוקצ'יין |
| [קריירה, חינוך ובריאות](./28-career-education-health/) | 45 | קורות חיים, ניהול קריירה, חונכות לימודית ובריאות אישית |
| [ECC (Everything Claude Code)](./29-ecc/) | 285 | חבילת affaan-m/ECC — 285 סקילים; ה-agents/rules/hooks/commands שלה בתיקיות הארטיפקטים |
| [אחר](./99-other/) | 0 | סקילים שלא סווגו לקטגוריה ברורה |
