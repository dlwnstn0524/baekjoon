a, b = input().split()
a = a[::-1]
b = b[::-1]

print(a, b)
for i in range(3):
    if ord(a[i]) - ord('0') > ord(b[i]) - ord('0'):
        print(a)
    elif ord(a[i]) - ord('0') > ord(b[i]) - ord('0'): 
        print(b)
    else :
        continue