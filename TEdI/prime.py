n = int(input())
answer = []

for i in range(2,n+1):
    for j in range(2,i+1):
        if j == i:
            answer.append(i)
        else :
            if i % j == 0 :
                break
            else :
                continue
print(*answer)