t = int(input())
for i in range(t):
    r, str = input().split()
    r = int(r)
    for j in str:
        for k in range(r) :
            print(j, end='')
    print()