import json
with open('sjsj.json', 'r') as students:
    sjsj_data=json.load(students)
    print(type(sjsj_data))
    print(sjsj_data)