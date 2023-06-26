input = list(input())

alpha = []
num = 0
for i in input:
    if ord("A") <= ord(i) <= ord("Z"):
        alpha.append(i)
    else:
        num += int(i)
alpha.sort()
if num != 0:
    alpha.append(str(num))

print(''.join(alpha))
    