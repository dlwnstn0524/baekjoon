n = int(input())
grade = list(map(int, input().split()))
max = 0
sum = 0
avg = 0

for i in grade :
    if max < i :
        max = i

for i in range(n):
    grade[i] = grade[i] / max * 100

for i in grade :
    sum += i

avg = sum / n
print(avg)
