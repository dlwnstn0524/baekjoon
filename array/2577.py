a = int(input())
b = int(input())
c = int(input())

mul = a*b*c
temp = 0
arr = []

for i in range(10): #init the array with every value is 0
    arr.append(0) 

for i in range(9) :
    temp = mul % 10
    mul = int(mul / 10)
    arr[temp] += 1
    if mul == 0 :
        break

for i in arr :
    print(i)
