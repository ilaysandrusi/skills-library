# Hooks (משותפים)

Runtime event handlers plus their `hooks.json` wiring — scripts that fire on session start, before/after a tool call, on stop, and so on.

> **זהירות:** הוקים הם קוד שסוכן קוד מריץ אוטומטית. תקרא הוק לפני שאתה מחבר אותו. `zero/zero-gemini/hooks.json` ובמיוחד הוקים שמורידים ריצת-זמן — בדוק לפני הפעלה.

**קבצים כאן:** 91 — מ-20 מקורות.

כל מה שנמצא בתיקייה הזאת הוא **hooks ברמת הריפו** — במעלה הזרם הוא משרת כמה סקילים במקביל, ולכן אי אפשר לשייך אותו לסקיל אחד. ארטיפקטים שכן שייכים לסקיל ספציפי הועברו לתוך תיקיית הסקיל עצמו (`<category>/<skill>/hooks/`).

בכל תיקיית מקור יש `SOURCE.md` עם הריפו במעלה הזרם, הנתיב, ה-commit והרישיון.

| מקור | קבצים | ריפו במעלה הזרם | רישיון |
|---|---|---|---|
| [`aaron-marketing/`](./aaron-marketing/) | 2 | [aaron-he-zhu/aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills) | Apache-2.0 |
| [`addyosmani/`](./addyosmani/) | 9 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`aegis/`](./aegis/) | 3 | [GanyuanRan/Aegis](https://github.com/GanyuanRan/Aegis) | MIT |
| [`ai-music-skills/`](./ai-music-skills/) | 3 | [bitwize-music-studio/claude-ai-music-skills](https://github.com/bitwize-music-studio/claude-ai-music-skills) | CC0-1.0 |
| [`aws-core/`](./aws-core/) | 2 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | Apache-2.0 |
| [`claude-bootstrap/`](./claude-bootstrap/) | 5 | [alinaqi/claude-bootstrap](https://github.com/alinaqi/claude-bootstrap) | MIT |
| [`claude-memory-kit/`](./claude-memory-kit/) | 5 | [awrshift/claude-memory-kit](https://github.com/awrshift/claude-memory-kit) | MIT |
| [`claude-seo/`](./claude-seo/) | 3 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | MIT |
| [`context-engineering-kit/`](./context-engineering-kit/) | 6 | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | GPL-3.0 |
| [`dev-agent-skills/`](./dev-agent-skills/) | 2 | [fvadicamo/dev-agent-skills](https://github.com/fvadicamo/dev-agent-skills) | MIT |
| [`digital-marketing-pro/`](./digital-marketing-pro/) | 2 | [indranilbanerjee/digital-marketing-pro](https://github.com/indranilbanerjee/digital-marketing-pro) | MIT |
| [`ecc/`](./ecc/) | 22 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | MIT |
| [`expo/`](./expo/) | 1 | [expo/skills](https://github.com/expo/skills) | MIT |
| [`honeydew/`](./honeydew/) | 5 | [honeydew-ai/honeydew-ai-coding-agents-plugins](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins) | Apache-2.0 |
| [`infrasity-dev-gtm/`](./infrasity-dev-gtm/) | 2 | [infrasity-labs/dev-gtm-claude-skills](https://github.com/infrasity-labs/dev-gtm-claude-skills) | MIT |
| [`microsoft/`](./microsoft/) | 2 | [microsoft/skills](https://github.com/microsoft/skills) | MIT |
| [`n8n-skills/`](./n8n-skills/) | 11 | [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) | MIT |
| [`superpowers/`](./superpowers/) | 2 | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`understand-anything/`](./understand-anything/) | 3 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | MIT |
| [`zero/`](./zero/) | 1 | [officialzeroxyz/zero-plugins](https://github.com/officialzeroxyz/zero-plugins) | NOASSERTION |

> אלה **לא** סקילים. ראה [`../ARTIFACTS.md`](../ARTIFACTS.md).
