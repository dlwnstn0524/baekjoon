n, x = input().split()
n = int(n)
x = int(x)
a = input().split()
for i in range(n):
    a[i] = int(a[i])

for i in range(n):
    if a[i] < x :
        print(a[i], end=' ')