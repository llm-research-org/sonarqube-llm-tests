import datetime

def check_event_timing(event_date, check_time):
    # event_date is a datetime.date object
    # check_time is a datetime.datetime object
    if event_date > check_time:
        print("Event is in the future!")
    else:
        print("Event has passed or is now.")

# Usage
today_date = datetime.date.today()  # datetime.date object
now_time = datetime.datetime.now()  # datetime.datetime object
check_event_timing(today_date, now_time)