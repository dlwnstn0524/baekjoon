num = list(map(int, input()))

result = num[0]
for i in range(1, len(num)):
    if result == 0 or num[i] == 0 or result == 1 or num[i] == 1:
        result += num[i]
    else :
        result *= num[i]
print(result)