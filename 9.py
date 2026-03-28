import datetime

def seconds_start(date_str):
    try:
        dt = datetime.datetime.strptime(date_str, "%m/%d/%Y %H:%M:%S")

        start_year = datetime.datetime(year=dt.year, month=1, day=1, hour=0, minute=0, second=0)

        delta = dt - start_year

        print(delta.total_seconds())

    except ValueError:
        print("Ошибка")

seconds_start("12/04/1990 13:12:12")