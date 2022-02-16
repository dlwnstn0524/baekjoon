n, m = map(int, input().split())
arr = []

def dfs() :
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, n+1) :
        if isOk(i):
            arr.append(i)
            dfs()
            arr.pop()

def isOk(num):
    for item in arr :
        if num < item :
            return False
    return True

dfs()
