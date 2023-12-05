import json

import requests

import requests

from requests.auth import HTTPBasicAuth

import auth

res = requests.get('https://api.rtt.io/api/v1/json/search/BGN', auth=HTTPBasicAuth(auth.Username, auth.Password))
result = json.loads(res.content)
print(result['location'])