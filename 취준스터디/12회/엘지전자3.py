from copy import deepcopy

def solution(heights):
    answer = 0
    n = len(heights)

    for i in range(n):
        m_left = [heights[i], i]
        m_right = [heights[i], i]

        for j in range(i-1, -1, -1):
            if m_left[0] <= heights[j]:
                if m_left[1] != i and m_left[0] == heights[j]:
                    m_left[1] = j
                else:
                    answer += 1
                    m_left[0] = heights[j]
                    m_left[1] = j

        for j in range(i+1, n):
            if m_right[0] <= heights[j]:
                if m_right[1] != i and m_right[0] == heights[j]:
                    m_right[1] = j
                else:
                    answer += 1
                    m_right[0] = heights[j]
                    m_right[1] = j
        
    return answer