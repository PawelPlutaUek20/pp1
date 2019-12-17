import json

with open('notowania.json', encoding='utf-8') as f:
    data = json.load(f)

with open('notowania.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
    
