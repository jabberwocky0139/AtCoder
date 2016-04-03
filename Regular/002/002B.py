# coding: utf-8
#f = open("inputB.txt")
#year, month, day = [int(i) for i in f.readline().split("/")]
import datetime
year, month, day = [int(i) for i in input().split("/")]
d = datetime.datetime(year, month, day)
delta = datetime.timedelta(days=1)

flag = False
while(not(flag)):
    res = (d.year/d.month)/d.day
    flag = res-int(res) == 0
    if flag:
        print("{0}/{1:02}/{2:02}".format(d.year, d.month, d.day))
    d += delta
