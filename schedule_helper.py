import gzip
import json
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
import auth
import config
import os


def is_new_timeTable():

    my_file = Path(config.workingDir +'/schedule.txt')
    # return true if no schedule exists locally
    if not my_file.is_file():
        return True
    else:
        with open(config.workingDir +'/schedule.txt') as f:
            first_line = f.readline().strip('\n')
            schedule_meta_data = json.loads(first_line)
            timestamp = schedule_meta_data['JsonTimetableV1']['timestamp']
            dt_object = datetime.fromtimestamp(timestamp)

            today = datetime.today()
            d1 = today.strftime("%d/%m/%Y")
            d2 = dt_object.strftime("%d/%m/%Y")
            print(d1, d2)
        if d1 != d2:
            return True
        else:
            return False


def get_freight_timetable():
    # get the freight timetable using curl
    curl_string = "curl -L -u '{}:{}' -o file.gz '{}'".format(auth.feed_username, auth.feed_password, config.freight_url)
    process = subprocess.Popen(curl_string, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(process.returncode)

    # extracting the .gz and write to text file
    with gzip.open('file.gz', 'rb') as f_in:
        with open('workingDir/schedule.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def read_schedule(station):
    count = 0
    uid = []
    f = open(config.workingDir +"/JsonSchedule.txt", "r")
    for x in f:
        if x.__contains__(station):
            train_movement = json.loads(x)
            uid.append(train_movement)
            count += 1

    print(len(uid))
    return uid

def clean_up():
    if os.path.exists(config.workingDir + '/' + config.JsonAssociation):
        os.remove(config.workingDir + '/' + config.JsonAssociation)

    if os.path.exists(config.workingDir + '/' + config.JsonSchedule):
        os.remove(config.workingDir + '/' + config.JsonSchedule)

    if os.path.exists(config.workingDir + '/' + config.schedule):
        os.remove(config.workingDir + '/' + config.schedule)

    if os.path.exists(config.workingDir + '/' + config.tiploc):
        os.remove(config.workingDir + '/' + config.tiploc)