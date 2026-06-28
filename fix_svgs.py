import glob
import os

svg_files = glob.glob('assets/fallback-*.svg')

for f in svg_files:
    with open(f, 'r') as file:
        lines = file.readlines()
    
    new_lines = []
    for line in lines:
        if '<svg width="1200" height="900" viewBox="0 0 1200 900"' in line:
            new_lines.append(line.replace('<svg width="1200" height="900" viewBox="0 0 1200 900"', '<svg width="1064" height="764" viewBox="68 68 1064 764"'))
        elif '<rect width="1200" height="900"' in line:
            continue
        else:
            new_lines.append(line)
            
    with open(f, 'w') as file:
        file.writelines(new_lines)
        
print("Fixed SVGs.")
