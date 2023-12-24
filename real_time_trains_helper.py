import json
from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth

import auth


def lib_request():
    api = RttApi(auth.Username, auth.Password)
    departures = api.search_station_departures('CLJ')
    print(departures.services)

def get_trains_at_station(station):
    #  get info about station
    res = requests.get('https://api.rtt.io/api/v1/json/search/{}'.format(station), auth=HTTPBasicAuth(auth.Username, auth.Password))
    result = json.loads(res.content)
    print(result)
    return result

def get_station_info():
    #  get info about station
    res = requests.get('https://api.rtt.io/api/v1/json/search/BHM', auth=HTTPBasicAuth(auth.Username, auth.Password))
    result = json.loads(res.content)
    print(result)


def get_service_info_today(service):
    today = datetime.today()
    d1 = today.strftime("%d/%m/%Y")
    day = today.strftime('%d')
    month = today.strftime('%m')
    year = today.strftime('%Y')

    res = requests.get('https://api.rtt.io/api/v1/json/service/{}/{}/{}/{}'.format(service, year, month, day),
                       auth=HTTPBasicAuth(auth.Username, auth.Password))
    print('https://api.rtt.io/api/v1/json/service/{}/{}/{}/{}'.format(service, year, month, day))
    result = json.loads(res.content)
    print(result)

def latest_info_on_train(service):
    today = datetime.today()
    d1 = today.strftime("%d/%m/%Y")
    day = today.strftime('%d')
    month = today.strftime('%m')
    year = today.strftime('%Y')

    res = requests.get('https://www.realtimetrains.co.uk/service/gb-nr:{}/{}-{}-{}/detailed'.format(service, year, month, day),
                       auth=HTTPBasicAuth(auth.Username, auth.Password))
    print('https://www.realtimetrains.co.uk/service/gb-nr:{}/{}-{}-{}/detailed'.format(service, year, month, day))


if __name__ == '__main__':
    latest_info_on_train('H02140')