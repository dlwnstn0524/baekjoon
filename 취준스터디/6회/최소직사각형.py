def solution(sizes):
    answer = 0
    x = []
    y = []
    for size in sizes:
        size.sort(reverse= True)
    for nx, ny in sizes:
        x.append(nx)
        y.append(ny)
    answer = max(x) * max(y)
    return answer