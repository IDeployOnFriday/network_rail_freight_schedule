import gzip
import json
import shutil
import subprocess
import auth

freight_url = 'https://publicdatafeeds.networkrail.co.uk/ntrod/CifFileAuthenticate?type=CIF_FREIGHT_FULL_DAILY&day=toc-full'
def get_freight_timetable():
    # get the freight timetable using curl
    curl_string = "curl -L -u '{}:{}' -o file.gz '{}'".format(auth.feed_username, auth.feed_password, freight_url)
    process = subprocess.Popen(curl_string, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(process.returncode)

    # extracting the .gz and write to text file
    with gzip.open('file.gz', 'rb') as f_in:
        with open('schedule.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def read_schedule(station):
    count = 0
    uid = []
    f = open("tmp/JsonSchedule.txt", "r")
    for x in f:
        if x.__contains__(station):
            train_movement = json.loads(x)
            uid.append(train_movement)
            count += 1

    print(len(uid))
    return uid