loc = input()
x, y = int(ord(loc[0]) - ord('a') + 1), int(loc[1])

count = 0
delta = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
for i, j in delta:
    nx, ny = x + i, y + j
    if 1 <= nx <=8 and 1 <= ny <=8:
        count += 1
print(count)