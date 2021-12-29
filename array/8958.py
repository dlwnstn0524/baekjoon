n = int(input())
dup = 1
score = 0

for i in range(n):
    str = input()
    for j in range(len(str)):
        if j == 0 :
            if str[j] == 'O' :
                score += dup
        else :
            if str[j] == 'O' :
                if str[j-1] == 'O':
                    dup += 1
                score += dup
            elif str[j] == 'X' :
                dup = 1
    print(score)
    score = 0
    dup =1