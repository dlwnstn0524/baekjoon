def combi(arr, n):
    result = []
    if n == 0:
        result = [[]]
        return result
    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for c in combi(rest_arr, n-1):
            result.append([elem] + c)
    return result

print(combi([1,2,3,4], 3))