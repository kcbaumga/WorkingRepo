import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/kcbaumga/WorkingRepo/main/datasets/cars/cars.csv")
print(data)
import os
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)
#os.environ['NO_PROXY'] = '127.0.0.1'
import requests
import re
df = pd.DataFrame(data)
url1 = 'http://127.0.0.1:8000/cars'
headers = {'Content-type':'application/json'}
result = df.to_json(orient='records')#, lines=True)
#"test.json",
import json
#parsed = json.loads(result)
#del parsed['index']
#json.dumps(parsed)
#print(parsed)


result = result.replace("[", "")
result=result.replace("]", "")
data =  '{['+"""{
  "carid": 2,
  "buying": "string",
  "maint": "string",
  "doors": "string",
  "persons": "string",
  "lug_boot": "string",
  "carsafety": "string",
  "decision": "string"
},
{
  "carid": 3,
  "buying": "string",
  "maint": "string",
  "doors": "string",
  "persons": "string",
  "lug_boot": "string",
  "carsafety": "string",
  "decision": "string"
}
"""+"]}"
requests.post(url=url1, data=data)
#print(result)
#x=requests.get(url,verify=False)
#print(x.text())
print(data)