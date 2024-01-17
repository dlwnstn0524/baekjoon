T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    pascal = [[1]]
    for i in range(N-1):
        temp = []
        front = [0] + pascal[i]
        back = pascal[i] + [0]
        for a, b in zip(front, back):
            temp.append(a + b)
        pascal.append(temp)
    
    print("#{}".format(test_case))
    for i in pascal:
        print(*i)