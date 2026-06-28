import json

def update_ids(filename, suffix):
    with open(filename, 'r') as f:
        data = json.load(f)
        
    new_sections = {}
    for key, val in data.get('sections', {}).items():
        if key == 'main':
            new_sections[key] = val
            continue
            
        new_key = f"{key}_{suffix}"
        
        if 'blocks' in val:
            new_blocks = {}
            for b_key, b_val in val['blocks'].items():
                new_b_key = f"{suffix}_{b_key}"
                new_blocks[new_b_key] = b_val
            val['blocks'] = new_blocks
            
        new_sections[new_key] = val
        
    data['sections'] = new_sections
    
    # Update order
    new_order = []
    for o in data.get('order', []):
        if o == 'main':
            new_order.append(o)
        else:
            new_order.append(f"{o}_{suffix}")
    data['order'] = new_order
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

update_ids('templates/page.app-industrial.json', 'ind')
update_ids('templates/page.app-commercial.json', 'com')
print("JSON updated")
