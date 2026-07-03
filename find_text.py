import os
import re

directories = ['sections', 'templates', 'snippets']
pattern = re.compile(r'(?<![-_\.])svarakshit(?![-_\.])', re.IGNORECASE)

for root, _, files in os.walk('.'):
    if not any(d in root for d in directories) and root != '.':
        continue
    for file in files:
        if file.endswith('.liquid') or file.endswith('.json'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                matches = pattern.finditer(content)
                for m in matches:
                    # extract the line
                    start = max(0, content.rfind('\n', 0, m.start()))
                    end = content.find('\n', m.end())
                    if end == -1:
                        end = len(content)
                    line = content[start:end].strip()
                    if 'id=' not in line and 'class=' not in line and 'SvarakshitContactForm' not in line:
                        print(f"{path}: {line}")
