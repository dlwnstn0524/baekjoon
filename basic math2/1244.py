import sys

def min(a,b) :
    if a > b :
        return b
    else :
        return a

n = int(sys.stdin.readline()) # number of switch
arr = list(map(int, sys.stdin.readline().split()))
t = int(sys.stdin.readline())
for i in range(t):

    gender, num = map(int, sys.stdin.readline().split())

    if gender == 1 :
        for i in range(n):
            if (i+1) % num == 0 :
                if arr[i] == 0 :
                    arr[i] = 1
                elif arr[i] == 1 :
                    arr[i] = 0

    if gender == 2 :
        for i in range(min(num-1, len(arr) - num)+1) :
            if arr[num-1-i] == arr[num-1+i] :
                if arr[num-1-i] == 0 :
                    arr[num-1-i] = 1
                    arr[num-1+i] = 1
                else :
                    arr[num-1-i] = 0
                    arr[num-1+i] = 0
            else : 
                break

for i in range(n):
    print(arr[i], end = ' ')
    if (i+1) % 20 == 0 :
        print()