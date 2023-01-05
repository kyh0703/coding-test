import datetime

hour, min, sec = map(int, input().split())
require = int(input())

s1 = (sec+require) % 60
m1 = (sec+require)//60
m2 = (min+m1) % 60
h1 = (min+m1)//60
h2 = (hour+h1) % 24

print(h2, m2, s1)  # 출력
