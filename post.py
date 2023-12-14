import gzip
import json
import os
import shutil
import subprocess
import requests
from datetime import date


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
    # get the freight timetable using curl
    curl_string = "curl -L -u '{}:{}' -o file.gz '{}'".format(auth.feed_username, auth.feed_password, freight_url)
    process = subprocess.Popen(curl_string, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(process.returncode)

    # extracting the .gz and write to text file
    with gzip.open('file.gz', 'rb') as f_in:
        with open('file.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def read_file():
    count = 0
    uid = []
    f = open("file.txt", "r")
    for x in f:
        if x.__contains__("CIF_train_uid"):
            train_movement = json.loads(x)
            uid.append(train_movement['JsonScheduleV1']['CIF_train_uid'])
            count += 1

    print(len(uid))
    return uid

def write_to_file(uid_list):
    f = open("uid.txt", "a")
    for item in uid_list:
        f.write("%s\n" % item)
    f.close()


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

def get_train_stops(service):

    # .....
    #  get info on specific service
    res = requests.get('https://api.rtt.io/api/v1/json/service/{}/2023/12/13'.format(service), auth=HTTPBasicAuth(auth.Username, auth.Password))
    result = json.loads(res.content)
    print(result)

# def get_service_info(service):
    # d1 = today.strftime("%d/%m/%Y")
    # day = today.strftime('%d')
    # month = today.strftime('%m')
    # year = today.strftime('%Y')
    #
    # res = requests.get('https://api.rtt.io/api/v1/json/service/{}/{}/{}/{}'.format(service, year, month, day ),
    #                    auth=HTTPBasicAuth(auth.Username, auth.Password))
    # result = json.loads(res.content)
    # print(result)


if __name__ == '__main__':
    get_freight_timetable()
    uid_list = read_file()
    write_to_file(uid_list)
    get_train_stops("C02569")