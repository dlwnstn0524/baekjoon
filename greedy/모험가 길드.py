n = int(input())
gongpo = list(map(int,input().split()))

group = 0
count = 0
gongpo.sort()

for i in gongpo:
    count += 1
    if count >= i:
        group += 1
        count = 0
print(group)


