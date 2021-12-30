n = int(input())
num = input()

sum = 0
for i in range(n):
    sum += ord(num[i]) - ord('0')

print(sum)