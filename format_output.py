import re
from datetime import datetime

from dates import is_date_between


def get_timetable(trains_passing, station):
    d1 = datetime.today()
    today = d1.strftime("%Y-%m-%d")
    print('today' + today)
    print('total scehdule trains to pass {} '.format(len(trains_passing)))
    ordered_trains = []
    for train in trains_passing:
        uid = train['JsonScheduleV1']['CIF_train_uid']
        schedule_end_date = train['JsonScheduleV1']['schedule_end_date']
        schedule_start_date = train['JsonScheduleV1']['schedule_start_date']
        schedule_locations = train['JsonScheduleV1']['schedule_segment']['schedule_location']

        for stop in schedule_locations:
            place = stop['tiploc_code']
            if place == station:

                if 'pass' in stop and stop['pass'] is not None:
                        time = re.sub("[^0-9]", "", stop['pass'])
                        if is_date_between(schedule_start_date, schedule_end_date,today):
                            ordered_trains.append([uid, place, time,schedule_start_date,schedule_end_date])

                if 'arrival' in stop and stop['arrival'] is not None:
                    time = re.sub("[^0-9]", "", stop['arrival'])
                    if is_date_between(schedule_start_date, schedule_end_date, today):
                        ordered_trains.append([uid, place, time, schedule_start_date, schedule_end_date])

    sorted_by_second = sorted(ordered_trains, key=lambda tup: tup[2])
    for t in sorted_by_second:
         print(t)
    print('total scehdule trains to schedules today {} ', len(ordered_trains))