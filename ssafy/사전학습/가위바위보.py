a, b = map(int, input().split())
case = [(1,2), (1,3), (2, 1), (2, 3), (3,1), (3,2)]
if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print("B")
else:
    print("A")