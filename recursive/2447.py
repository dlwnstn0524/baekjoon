def star(n):
    if n == 3:
        Map[0][:3] = Map[2][:3] = [1,1,1]
        Map[1][:3] = [1,0,1]
        return
    star(n//3)
    temp = n//3
    for i in range(3) :
        for j in range(3):
            if i == 1 and j == 1 :
                continue
            for k in range(temp):
                Map[temp*i+k][temp*j:temp*j+temp] = Map[k][:temp]


        

n = int(input())
Map = [[0 for i in range(n)] for j in range(n)]
star(n)
for i in range(n):
    for j in range(n):
        if Map[i][j] == 1:
            print("*",end='')
        else:
            print(" ",end='')
    print()
