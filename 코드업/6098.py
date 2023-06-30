maps = []
for i in range(10):
    maps.append(list(map(int, input().split())))

x, y = 1, 1

while True:
    if (maps[x][y] == 0):
        maps[x][y] = 9
    elif (maps[x][y] == 2):
        maps[x][y] = 9
        break

    if ((maps[x][y+1] == 1 and maps[x+1][y] == 1)):
        break

    if (maps[x][y+1] != 1):
        y = y + 1
    elif (maps[x+1][y] != 1):
        x = x + 1

for i in range(10):
    for j in range(10):
        print(maps[i][j], end=' ')
    print()
