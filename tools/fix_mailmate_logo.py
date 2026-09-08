from pathlib import Path
import re

path = Path("docs/index.html")
text = path.read_text(encoding="utf-8")

new_css = '''        .mm-logo {
            width: 58%;
            height: 58%;
            display: block;
            object-fit: contain;
            border-radius: 0;
            transform: translateZ(35px);
            filter: drop-shadow(0 18px 30px rgba(0,0,0,.38));
            user-select: none;
            -webkit-user-drag: none;
        }'''

text, css_count = re.subn(r"(?ms)^\s*\.mm-logo\s*\{.*?^\s*\}", new_css, text, count=1)
if css_count != 1:
    raise SystemExit(f"Expected one .mm-logo CSS block, found {css_count}")

old_src = "https://raw.githubusercontent.com/sphereofrupayan/CipherSquad/main/assets/images/cs_logo.png"
new_src = "./images/mailmate-mark.svg?v=1"
if old_src not in text:
    raise SystemExit("Current MailMate logo source not found")
text = text.replace(old_src, new_src, 1)

path.write_text(text, encoding="utf-8")
