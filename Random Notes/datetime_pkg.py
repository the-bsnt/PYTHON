from datetime import datetime

t1 = "Sat 02 May 2015 19:54:36 +0530"
t2 = "Fri 01 May 2015 13:54:36 -0000"
fmt = "%a %d %b %Y %H:%M:%S %z"

# .strptime() will parse the string into datetime object in required form+at
dt1 = datetime.strptime(t1, fmt)
dt2 = datetime.strptime(t2, fmt)

# datetime.strftime() will change the format of the date. only apply on datetime object
fmt2 = "%d %b %Y"
formated_date = datetime.strftime(dt1, fmt2)
print("formated time: ", formated_date)

# & dt1-dt2 is timedelta object which is used to represent duration.
print("Time difference:", (dt1 - dt2))

# & .total_seconds() converts the duration to all seconds.
print("Time difference:", int((dt1 - dt2).total_seconds()))


#! converts minutes of duration into seconds.
print("Time difference:", int((dt1 - dt2).seconds))
print("Time difference:", int((dt1 - dt2).days))
print("Time difference:", int((dt1 - dt2).microseconds))
