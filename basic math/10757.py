a, b = input().split()
a = "".join(reversed(a))
b = "".join(reversed(b))
result = [0 for i in range(len(max(a,b))+1)]


for i in range(len(result)-1) :
    result[i] = ord(a[i]) + ord(b[i]) - 2*ord('0') + result[i]
    if result[i] >= 10 :
        result[i+1] += 1
        result[i] -= 10

if result[len(result) - 1]  == 0 :
    result.pop()

for i in range(len(result)):
    print(result[len(result)-1-i], end = '')