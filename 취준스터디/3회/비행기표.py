def solution(tickets):
    answer = []
    tickets.sort(key = lambda x : (x[0], x[1]))
    used = [False for _ in range(len(tickets))]
    stack = []
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            stack.append(tickets[i])
            used[i] = True
            answer.append(tickets[i][0])
            break
    while stack:
        ticket = stack.pop()
        print(ticket)
        idx = tickets.index(ticket)
        used[idx] = True
        if False not in used:
            answer.append(tickets[idx][1])
        start, end = ticket[0], ticket[1]
        for i in range(len(tickets)):
            if tickets[i][0] == end and used[i] == False:
                stack.append(tickets[i])
                answer.append(tickets[i][0])
    return answer