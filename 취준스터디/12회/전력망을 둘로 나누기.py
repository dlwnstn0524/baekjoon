def dfs(start_node, adj_list, n):  # dfs 로직
    visited = set()
    stack = [start_node]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)

            for destination in adj_list[current]:
                if destination not in visited:
                    stack.append(destination)

    return abs(len(visited)*2-n)  # 첫 번째 테스트케이스에서 한 덩어리가 3개가 나왔다면 3과 9(n)-3의(6의) 차이를 구해야 하므로.

def solution(n, wires):
    answer = 101
    adj_list = [[] for _ in range(n+1)]

    for start, end in wires:  # 인접 리스트 완성
        adj_list[start].append(end)
        adj_list[end].append(start)

    for n1, n2 in wires:  # 간선의 갯수만큼 돌면서, 하나씩 끊어보고 dfs
        cut1 = adj_list[n1].pop(adj_list[n1].index(n2))
        cut2 = adj_list[n2].pop(adj_list[n2].index(n1))
        answer = min(answer, dfs(n1, adj_list, n))
        adj_list[cut1].append(cut2) # 복원
        adj_list[cut2].append(cut1)

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))  # 3
print(solution(4, [[1, 2], [2, 3], [3, 4]]))  # 0
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))  # 1