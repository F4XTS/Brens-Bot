import json
contents = []

try:
    with open("./Epic/Discord/archive.json", 'r') as f:
        contents = json.load(f)
except Exception as e:
    print(e)


li = [item.get('templateId') for item in contents]
print(li)