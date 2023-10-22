def solution(loans):
    answer = []
    lim = 0

    for i in range(len(loans)):
        # 대출 한도에 직장 등급 반영
        lim = loans[i][2] * (6 - loans[i][0])
        
        # 대출 한도에 신용 등급 반영
        if loans[i][1] == 1:
            lim += 1000
        elif loans[i][1] == 2:
            lim += 500
        elif loans[i][1] == 3:
            lim += 300
        elif loans[i][1] == 4:
            lim += 100
        elif loans[i][1] == 5:
            lim += 0
        
        if loans[i][3] + loans[i][4] <= lim:
            answer.append(1)
        elif loans[i][3] + loans[i][4] > lim:
            answer.append(0)

    return answer