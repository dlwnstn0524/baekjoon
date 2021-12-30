def function(a): #Funtion to check it is self number.
    temp = a
    ans = 0
    while True :
        if a == 0 :
            break
        else :
            ans += a % 10
            a = int (a / 10)
    ans += temp
    return ans

arr = [0 for i in range(10000)]

for i in range(1, 10000) :
    if function(i) < 10000 :
        arr[function(i)] = 1

for i in range(1, 10000) :
    if arr[i] == 0 :
        print(i)