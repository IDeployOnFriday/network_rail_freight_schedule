import config
from format_output import get_timetable
from get_station_timetable import get_trains_passing_today
from schedule_helper import get_freight_timetable, is_new_timeTable, read_schedule
from preprocess_files import split_files


'''
station options for testing 
YORK 
BRGEND
'''


if __name__ == '__main__':

    config.station = 'YORK'
    # station = input("Enter station short code to get schedule:")
    print("getting freight schedule for : " + config.station + " station")

    if is_new_timeTable():
        clear_up()
        get_freight_timetable()
        split_files()

    trains_passing = read_schedule(config.station)
    (running_trains, not_running_trains) = get_trains_passing_today(trains_passing)

    print('Number of trains running {} '.format(len(running_trains)))
    print('Number of trains not running {} '.format(len(not_running_trains)))

    get_timetable(running_trains, config.station)

