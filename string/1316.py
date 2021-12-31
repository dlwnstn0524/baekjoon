n = int(input())
cnt = n

for i in range(n) :
    word = input()
    arr = [0 for i in range(ord('z')- ord('a') + 1)]
    for i in range(len(word)):
        if arr[ord(word[i])-ord('a')] == 1:
            if word[i-1] == word[i] :
                continue
            else :
                cnt -= 1
                break
        elif arr[ord(word[i])-ord('a')] == 0 :
            arr[ord(word[i]) - ord('a')] = 1
        
print(cnt)
