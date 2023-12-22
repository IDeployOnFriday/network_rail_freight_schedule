from datetime import datetime


def is_date_between(start_date, end_date, my_date):

    s_date = datetime.strptime(start_date, '%Y-%m-%d')
    e_date = datetime.strptime(end_date, '%Y-%m-%d')
    my_date = datetime.strptime(my_date, '%Y-%m-%d')

    if s_date <= my_date <= e_date:
        return True
    else:
        return False