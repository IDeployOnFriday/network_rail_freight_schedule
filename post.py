import json

import requests

import requests

from requests.auth import HTTPBasicAuth

import auth

#  get info about station
res = requests.get('https://api.rtt.io/api/v1/json/search/BGN', auth=HTTPBasicAuth(auth.Username, auth.Password))
result = json.loads(res.content)
print(result)

# .....
#  get info on specific service
res = requests.get('https://api.rtt.io/api/v1/json/service/H06145/2023/12/06', auth=HTTPBasicAuth(auth.Username, auth.Password))
result = json.loads(res.content)
print(result)