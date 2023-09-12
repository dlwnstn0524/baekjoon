def solution(picks, minerals):
    # 광물들 5개씩 끊기
    minerals_divided = list_divided(minerals, 5)

    # 곡갱이 종류별로 사용했을 때 피로도 계산
    costs = []  # 피로도 종합
    for section in minerals_divided:
        cost = [0, 0, 0]  # 다이아몬드, 철, 돌 곡갱이를 사용했을 때 피로도
        for mineral in section:
            if mineral == "diamond":  # 다이아몬드 광석을 캘 경우
                cost[0] += 1
                cost[1] += 5
                cost[2] += 25
            elif mineral == "iron":  # 철 광석을 캘 경우
                cost[0] += 1
                cost[1] += 1
                cost[2] += 5
            else:  # 돌을 캘 경우
                cost[0] += 1
                cost[1] += 1
                cost[2] += 1
        costs.append(cost)
    else:
        while len(costs) > sum(picks):  # 곡갱이 숫자보다 더 많은 광물을 캘 수 없음
            costs.pop()
    # 피로도 최소값 계산
    costs_sorted = sorted(costs, key=lambda x: x[2], reverse=True)
    cost_integrated = 0
    for cost in costs_sorted:
        if picks[0] > 0:
            cost_integrated += cost[0]
            picks[0] -= 1
            continue

        if picks[1] > 0:
            cost_integrated += cost[1]
            picks[1] -= 1
            continue

        if picks[2] > 0:
            cost_integrated += cost[2]
            picks[2] -= 1

    return cost_integrated


def list_divided(target_list: list, n: int):
    return [target_list[i:i+n] for i in range(0, len(target_list), n)]