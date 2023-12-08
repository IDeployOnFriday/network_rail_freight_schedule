import json

import requests

import requests

from requests.auth import HTTPBasicAuth

import auth
from rttapi.api import RttApi

freight_url = 'https://publicdatafeeds.networkrail.co.uk/ntrod/CifFileAuthenticate?type=CIF_FREIGHT_FULL_DAILY&day=toc-full'

def lib_request():
    api = RttApi(auth.Username, auth.Password)
    departures = api.search_station_departures('CLJ')
    print(departures.services)

def get_freight_timetable():
    res = requests.get(freight_url,  auth=HTTPBasicAuth(auth.feed_username, auth.feed_password))

def curl_request():
    #  get info about station
    res = requests.get('https://api.rtt.io/api/v1/json/search/BGN', auth=HTTPBasicAuth(auth.Username, auth.Password))
    result = json.loads(res.content)
    print(result)

    # .....
    #  get info on specific service
    res = requests.get('https://api.rtt.io/api/v1/json/service/H31618/2023/12/07', auth=HTTPBasicAuth(auth.Username, auth.Password))
    result = json.loads(res.content)
    print(result)

if __name__ == '__main__':
    get_freight_timetable()