import json

import requests

import requests

from requests.auth import HTTPBasicAuth

import auth
from rttapi.api import RttApi



def lib_request():
    api = RttApi(auth.Username, auth.Password)
    departures = api.search_station_departures('CLJ')
    print(departures.services)


def curl_request():
    #  get info about station
    res = requests.get('https://api.rtt.io/api/v1/json/search/BGN', auth=HTTPBasicAuth(auth.Username, auth.Password))
    result = json.loads(res.content)
    print(result)

    # .....
    #  get info on specific service
    res = requests.get('https://api.rtt.io/api/v1/json/service/H06145/2023/12/06', auth=HTTPBasicAuth(auth.Username, auth.Password))
    result = json.loads(res.content)
    print(result)

if __name__ == '__main__':
    lib_request()