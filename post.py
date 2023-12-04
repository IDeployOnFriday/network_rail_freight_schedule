import requests

import requests

from requests.auth import HTTPBasicAuth

import auth

res = requests.get('https://api.rtt.io/api/v1/json/search/BMH', auth=HTTPBasicAuth(auth.Username, auth.Password))
print(res.content)