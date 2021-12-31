a, b, v = map(int, input().split())
h = 0
day = 0

while True :
    h += a
    day += 1
    if h >= v:
        print(day)
        break
    h -= b