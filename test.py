from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    frmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, frmt)
    dt2 = datetime.strptime(t2, frmt)
    return str(int((dt1 - dt2).total_seconds()))


t = int(input())
for t_itr in range(t):
    t1 = input()
    t2 = input()
    delta = time_delta(t1, t2)
    print(delta)
