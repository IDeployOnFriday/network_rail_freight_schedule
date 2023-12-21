import re

def get_timetable(trains_passing):
    ordered_trains = []
    for train in trains_passing:
        uid = train['JsonScheduleV1']['CIF_train_uid']
        schedule_locations = train['JsonScheduleV1']['schedule_segment']['schedule_location']
        for stop in schedule_locations:
            place = stop['tiploc_code']
            if place == 'BRGEND':
                try:
                    time = re.sub("[^0-9]", "", stop['pass'])
                    print('{} Passing {} : {}'.format(uid, place, time))
                    ordered_trains.append([uid, place, time])
                except:
                    print("An exception occurred")

    tmp = [('a', 'b', '011'),('a', 'b', '120'),('a', 'b', '015')]

    sorted_by_second = sorted(ordered_trains, key=lambda tup: tup[2])
    for t in sorted_by_second:
        print(t)
