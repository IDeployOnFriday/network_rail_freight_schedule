
from datetime import datetime

def get_trains_passing_today(trains_passing):
    running_trains = []
    not_running_trains = []
    today_dateNumber = datetime.today().weekday()
    for train in trains_passing:
        uid = train['JsonScheduleV1']['CIF_train_uid']
        days_running = train['JsonScheduleV1']['schedule_days_runs']
        schedule_end_date = train['JsonScheduleV1']['schedule_end_date']
        schedule_start_date = train['JsonScheduleV1']['schedule_start_date']
        if days_running[today_dateNumber] == '1':
            running_trains.append(train)

        else:
            not_running_trains.append(train)
        #get_service_info(uid)

    print(len(running_trains))
    return (running_trains, not_running_trains)