import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for node in data['nodes']:
    if 'attributes' in node and 'street_name' in node['attributes']:
        node['label'] = node['attributes']['street_name']

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)