input = input()
sum = 0

for i in input :
    if i >= 'A' and i <= 'C' :
        sum += 3
    if i >= 'D' and i <= 'F' :
        sum += 4
    if i >= 'G' and i <= 'I' :
        sum += 5
    if i >= 'J' and i <= 'L' :
        sum += 6
    if i >= 'M' and i <= 'O' :
        sum += 7
    if i >= 'P' and i <= 'S' :
        sum += 8
    if i >= 'T' and i <= 'V' :
        sum += 9
    if i >= 'W' and i <= 'Z' :
        sum += 10

print(sum)
