T = int(input())
for test_case in range(1, T+1):
    answer = 0
    flag = True
    puzzle = []

    for _ in range(9):
        temp = list(map(int, input().split()))
        puzzle.append(temp)
    
    for i in range(9):
        if sum(puzzle[i]) != 45:
            flag = False
            break
        
    for i in zip(*puzzle):
        if sum(list(i)) != 45:
            flag = False
            break
    
    for i in range(3):
        t = puzzle[i*3:i*3+3]
        for j in range(3):
            temp = []
            temp = temp + t[0][j*3:j*3+3] + t[1][j*3:j*3+3] + t[2][j*3:j*3+3]
            if sum(temp) != 45:
                flag = False
                break
    if flag:
        answer = 1
    print("#{} {}".format(test_case, answer))