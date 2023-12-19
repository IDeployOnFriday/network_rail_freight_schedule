from format_output import get_timetable
from get_station_timetable import get_trains_passing_today
from schedule_helper import get_freight_timetable, read_schedule
from preprocess_files import split_files


'''
station options for testing 
YORK 
BGN
'''


if __name__ == '__main__':
    # get_freight_timetable()
    # split_files()
    trains_passing = read_schedule('BGN')
    (running_trains, not_running_trains) = get_trains_passing_today(trains_passing)

    print('Number of trains running {} '.format(len(running_trains)))
    print('Number of trains not running {} '.format(len(not_running_trains)))

    get_timetable(running_trains)

