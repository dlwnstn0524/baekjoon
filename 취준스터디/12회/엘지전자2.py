def solution(fruits, priority):
    answer = []
    feature = []
    m = len(priority[0])

    for i in zip(fruits, priority):
        temp = []
        for j in zip(i[0], i[1]):
            temp.append(j)
        temp.sort(key = lambda x : x[1])
        t = []
        for k in range(m):
            t.append(temp[k][0])
        feature.append(t)
    
    feature_sorted = sorted(feature, reverse= True)
    
    for i in feature_sorted:
        answer.append(feature.index(i)+1)
    
    return answer