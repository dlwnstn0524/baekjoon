def solution(sizes):
    answer = 0
    m_list = []
    M_list = []
    for size in sizes:
        temp = sorted(size)
        m_list.append(temp[0])
        M_list.append(temp[1])
    answer = max(m_list) * max(M_list)
    return answer