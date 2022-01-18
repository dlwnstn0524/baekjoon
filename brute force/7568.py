n = int(input())
group = []
temp = 0
rank = [0 for i in range(n)]

for i in range(n):
    member = list((map(int, input().split())))
    group.append(member)

for i in group :
    for j in group :
        if i == j :
            continue
        else :
            if i[0] < j[0] and i[1] < j[1]:
                rank[temp] += 1
    temp += 1
    

for i in rank :
    print(i+1, end=' ')
                