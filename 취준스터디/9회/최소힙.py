N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0 :
            print(0)
        else:
            print(heap.pop())
    else:
        heap.append(x)
        heap.sort(reverse=True)