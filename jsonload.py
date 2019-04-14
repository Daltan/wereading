import json
def loadinfo():
    with open('./info.json',encoding='utf8') as f:
        content = json.load(f)
        return content
print(loadinfo()['appname'])
