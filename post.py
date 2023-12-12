import json
import zipfile, io
import requests
from datetime import date

import today
from requests.auth import HTTPBasicAuth

import auth
from rttapi.api import RttApi

freight_url = 'https://publicdatafeeds.networkrail.co.uk/ntrod/CifFileAuthenticate?type=CIF_FREIGHT_FULL_DAILY&day=toc-full'
freight_url_CIF = 'https://publicdatafeeds.networkrail.co.uk/ntrod/CifFileAuthenticate?type=CIF_FREIGHT_FULL_DAILY&day=toc-full.CIF.gz'
rtt_url='https://api.rtt.io/api/v1/json/search/'

def lib_request():
    api = RttApi(auth.Username, auth.Password)
    departures = api.search_station_departures('CLJ')
    print(departures.services)

def get_freight_timetable():
    r = requests.get(freight_url,  auth=HTTPBasicAuth(auth.feed_username, auth.feed_password))

def get_trains_at_station(station):
    #  get info about station
    res = requests.get('https://api.rtt.io/api/v1/json/search/{}'.format(station), auth=HTTPBasicAuth(auth.Username, auth.Password))
    result = json.loads(res.content)
    print(result)
    return result

def curl_request():

    #  get info about station
    res = requests.get('https://api.rtt.io/api/v1/json/search/BHM', auth=HTTPBasicAuth(auth.Username, auth.Password))
    result = json.loads(res.content)
    print(result)

    # .....
    #  get info on specific service
    res = requests.get('https://api.rtt.io/api/v1/json/service/H31618/2023/12/07', auth=HTTPBasicAuth(auth.Username, auth.Password))
    result = json.loads(res.content)
    print(result)

def get_service_info(service):
    d1 = today.strftime("%d/%m/%Y")
    day = today.strftime('%d')
    month = today.strftime('%m')
    year = today.strftime('%Y')

    res = requests.get('https://api.rtt.io/api/v1/json/service/{}/{}/{}/{}'.format(service, year, month, day ),
                       auth=HTTPBasicAuth(auth.Username, auth.Password))
    result = json.loads(res.content)
    print(result)


if __name__ == '__main__':
    get_freight_timetable()