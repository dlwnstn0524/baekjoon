str = input()
arr = [-1 for i in range(ord('z')- ord('a') + 1)]
for i in range(len(str)) :
    if arr[ord(str[i]) - ord('a')] == -1 :
        arr[ord(str[i]) - ord('a')] = i

for i in arr :
    print(i, end=' ')