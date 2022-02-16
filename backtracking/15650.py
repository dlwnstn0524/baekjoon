n, m = map(int, input().split())
arr = []
def dfs():
    if len(arr) == m :
        print(' '.join(map(str, arr))) # arr안에 있는 요소들을 띄어쓰기를 포함하여 출력
        return

    for i in range(1, n+1):
        if isOk(i):
            arr.append(i)
            dfs()
            arr.pop()

def isOk(i):
    for item in arr :
        if i <= item :
            return False
    return True
    
dfs()