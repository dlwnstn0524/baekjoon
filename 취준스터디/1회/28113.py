n, a, b = map(int, input().split())
if n <= b:
    if a < b:
        print("Bus")
    elif a == b:
        print("Anything")
    else :
        print("Subway")
else :
    print("Bus")