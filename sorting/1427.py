a = input()
num = []
for i in a:
    num.append(int(i))
num.sort()
num.reverse()
for i in num :
    print(i, end='')