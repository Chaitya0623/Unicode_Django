from os import name
import requests

url = "https://demo.stepzen.net/studio/spacex/__graphql"

payload="{\"query\":\"query MyQuery {\\n  spacex_missions(limit: 10) {\\n    id\\n    manufacturers\\n    name\\n  }\\n}\",\"variables\":{}}"
headers = {
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload).json()

data = response.get('data').get('spacex_missions')

for i in data:
    print(i)

# resop = {}
# req = modelname['field name' = hhjg, ]