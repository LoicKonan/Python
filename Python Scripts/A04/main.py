import json, re

all_ips =[]

with open('manifest.json', 'r') as json_file:
    data = json.load(json_file)
    for item in data['items']:
        if 'ip' in item:
            all_ips.append(item['ip'])
        else:
            all_ips.append(item['ipv4'])
data = json_load['objects']
for x in data:
    print(json.dumps(json_load['objects'][0]['pattern'], indent=4))
