# import json

# json_data = '{"python": 1, "php": 2, "c": 3, "vb": 4, "perl": 5}'
# json_load = (json.loads(json_data))
# print(json.dumps(json_load, indent=4))


# # print a new line
# print("\n")
# print("\n")

# for x in json_load:
# 	print("%s: %d" % (x, json_load[x]))
 

# # print a new line
# print("\n")
# print("\n")

# with open('json_data.json', 'r') as json_file:
# 	json_load = json.load(json_file)

# print(json.dumps(json_load, indent=4))


# print(json.dumps(json_load['web']['languages'][0], indent=4))

import json

with open('json_data.json', 'r') as json_file:
	json_load = json.load(json_file)

data = json_load['web']['languages']
for x in data:
	print(x['id'], x['name'], x['website'])