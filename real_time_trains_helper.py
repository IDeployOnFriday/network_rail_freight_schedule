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
    result = json.loads(res.content)
    print(result)