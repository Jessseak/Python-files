import json
celebrities = '''
{
    "celebrities":[
    {
    "firstname": "Justin",
    "lastname": "Beiber",
    "job": "musician"
    },
    {"firstname": "Hailey",
    "lastname": "steinfield",
    "job": "Actress/popsinger"
    },
      { 
      "firstname": "Cristiano",
       "lastname": "Ronaldo",
        "job": "sportsman"
    },
     {   
      "firstname": "rodarius",
      "lastname": "green",
      "job": "musician"
      }
    ]
}
'''

info = json.loads(celebrities)
for celeb in info['celebrities']:
    print(celeb["job"])