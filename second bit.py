import json
with open("NBA homework.json",'r') as players:
    NBA=json.load(players)
    print(type(NBA))
    print(NBA)

