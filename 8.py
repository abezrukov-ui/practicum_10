import datetime

def f_datetime(date_str):

    try:
        dt = datetime.datetime.strptime(date_str, "%m/%d/%Y %H:%M:%S")

        date_p = dt.strftime("%d.%m.%y")

        time_p = dt.strftime("%I:%M:%S %p")

        print(f"{date_p} {time_p}")

    except ValueError:
        print("Ошибка")
        
f_datetime("13/04/1990 13:12:12")
