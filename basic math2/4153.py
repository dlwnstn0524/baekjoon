
while True :
    a, b, c= map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else :
        max = 0 
        max_i = 0
        sum = 0
        list = []
        list.append(a)
        list.append(b)
        list.append(c)
        for i in range(len(list)) :
            if max < list[i] :
                max = list[i]
                max_i = i
        for i in range(3):
            list[i] = list[i]**2
        
        for i in range(3):
            if i != max_i:
                sum += list[i]
        if sum == list[max_i] :
            print("right")
        else :
            print("wrong")

        