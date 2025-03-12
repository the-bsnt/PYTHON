from datetime import datetime

t1 = "Sat 02 May 2015 19:54:36 +0530"
t2 = "Fri 01 May 2015 13:54:36 -0000"
fmt = "%a %d %b %Y %H:%M:%S %z"

dt1 = datetime.strptime(t1, fmt)
# .strptime() will parse the string into datetime object in required form+at
dt2 = datetime.strptime(t2, fmt)


print("Time difference:", int((dt1 - dt2).total_seconds()))
