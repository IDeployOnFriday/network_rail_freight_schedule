

def get_timetable(trains_passing):
    for train in trains_passing:
        uid = train['JsonScheduleV1']['CIF_train_uid']
        schedule_locations = train['JsonScheduleV1']['schedule_segment']['schedule_location']
        for stop in schedule_locations:
            place = stop['tiploc_code']
            time = stop['departure']