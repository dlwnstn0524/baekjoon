n = int(input())
member = []

for i in range(n):
    age, name = map(str ,input().split())
    member.append([int(age), name])

member.sort(key = lambda x : x[0])

for i in range(n):
    print(member[i][0], member[i][1])