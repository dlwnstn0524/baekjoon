a, b = input().split()
a = a[::-1]
b = b[::-1]

for i in range(3):
    if a[i]> b[i]:
        print(a)
        break
    elif a[i] < b[i]: 
        print(b)
        break
    else :
        continue