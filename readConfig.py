import json

def readFile(filePath):
    with open(filePath) as json_data:
        data = json.load(json_data)
        return data