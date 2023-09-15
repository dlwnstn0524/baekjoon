N = int(input())
for _ in range(N):
    heap = []
    x = int(input())
    if x == 0:
        if len(heap) == 0 :
            print(0)
        else:
            m = min(heap)
            heap.pop(m)
            print(m)
    else:
        heap.append(x)
