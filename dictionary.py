import json
employees = '''
{
    "employees":[
    {
        "first_name":"David",
        "last_name":"Nate"
    },
    { 
      "first_name":"Mary",
        "last_name":"David"
    }
    ]
}
'''
print(employees)
data = json.loads(employees)
print(data)
for employee in data['employees']:
    print(employee["last_name"])