import sys
from _datetime import  datetime #날짜 함수
from datetime import timedelta

s_day = datetime(2014, 4, 2)
n = int(sys.stdin.readline())

d_day = s_day + timedelta(days=n-1)
d_day = d_day.strftime('%Y-%m-%d')
print(d_day)