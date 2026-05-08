import re

with open('/home/plutodev/Documents/deel/index.html', 'r') as f:
    content = f.read()

pattern = re.compile(
    r'<div class="d-flex flex-column align-items-start mt-3 gap-3">\s*'
    r'<div>\s*'
    r'(<img[^>]+>)\s*'
    r'(<p[^>]*>.*?</p>)\s*'
    r'</div>\s*'
    r'(<a href="#" class="btn btn-outline-dark rounded-pill px-4 flex-shrink-0"[\s\S]*?>Learn more &rarr;</a>)\s*'
    r'</div>',
    re.DOTALL
)

def repl(match):
    img = match.group(1)
    p = match.group(2)
    a = match.group(3)
    
    return f"""<div class="d-flex flex-column mt-3">
                        {img}
                        <div class="d-flex flex-column flex-lg-row align-items-start align-items-lg-center gap-3 mt-3">
                            {p}
                            {a}
                        </div>
                    </div>"""

new_content = pattern.sub(repl, content)

with open('/home/plutodev/Documents/deel/index.html', 'w') as f:
    f.write(new_content)

print(f"Replaced {len(pattern.findall(content))} occurrences.")
