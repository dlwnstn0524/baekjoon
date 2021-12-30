str = input()
arr = [0 for i in range(ord('z') - ord('a')+1)]
index = 0
max = 0
cnt = 0

for i in range(len(str)):
    if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z') :
        arr[ord(str[i])-ord('a')] += 1
    elif ord(str[i]) >= ord('A') and ord(str[i]) <= ord('Z') :
        arr[ord(str[i])-ord('A')] += 1

for i in range(len(arr)):
    if max < arr[i] :
        max = arr[i]
        index = i

for i in range(len(arr)):
    if max == arr[i] :
        cnt += 1

if cnt == 1 :
    print(chr(index+ord('A')))
else :
    print("?")