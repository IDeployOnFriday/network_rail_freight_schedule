import re

from dates import is_date_between


def get_timetable(trains_passing):
    print('total scehdule trains to pass {} '.format(len(trains_passing)))
    ordered_trains = []
    for train in trains_passing:
        uid = train['JsonScheduleV1']['CIF_train_uid']
        schedule_end_date = train['JsonScheduleV1']['schedule_end_date']
        schedule_start_date = train['JsonScheduleV1']['schedule_start_date']

        schedule_locations = train['JsonScheduleV1']['schedule_segment']['schedule_location']
        for stop in schedule_locations:
            place = stop['tiploc_code']
            if place == 'BRGEND':
                try:
                    time = re.sub("[^0-9]", "", stop['pass'])
                    #print('{} Passing {} : {}'.format(uid, place, time))
                    my_date='2023-12-23'
                    if is_date_between(schedule_start_date, schedule_end_date,my_date):
                        ordered_trains.append([uid, place, time,schedule_start_date,schedule_end_date])
                except:
                    print("An exception occurred")

    sorted_by_second = sorted(ordered_trains, key=lambda tup: tup[2])
    for t in sorted_by_second:
         print(t)
    print('total scehdule trains to schedules today {} ', len(ordered_trains))