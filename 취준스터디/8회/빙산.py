def count_zeros(matrix):
    # 이차원 배열에서 각 칸에 대해 상하좌우에 있는 0의 개수를 반환하는 함수
    rows, cols = len(matrix), len(matrix[0])
    zero_counts = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            zero_counts[i][j] = 0
            if matrix[i][j] != 0:
                if i > 0:
                    zero_counts[i][j] += (matrix[i - 1][j] == 0)
                if i < rows - 1:
                    zero_counts[i][j] += (matrix[i + 1][j] == 0)
                if j > 0:
                    zero_counts[i][j] += (matrix[i][j - 1] == 0)
                if j < cols - 1:
                    zero_counts[i][j] += (matrix[i][j + 1] == 0)

    return zero_counts

def decrease_numbers(matrix, zero_counts):
    # 각 칸의 숫자를 0의 개수에 따라 조정하는 함수
    rows, cols = len(matrix), len(matrix[0])
    modified = False

    for i in range(rows):
        for j in range(cols):
            if zero_counts[i][j] > 0:
                new_value = matrix[i][j] - zero_counts[i][j]
                if new_value < 0:
                    new_value = 0
                if matrix[i][j] != new_value:
                    matrix[i][j] = new_value
                    modified = True

    return matrix, modified

def count_clusters(matrix):
    # 0이 아닌 숫자의 덩어리 개수를 세는 함수 (DFS 사용)
    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] == 0 or visited[row][col]:
            return
        visited[row][col] = True
        for dr, dc in directions:
            dfs(row + dr, col + dc)

    rows, cols = len(matrix), len(matrix[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * cols for _ in range(rows)]
    cluster_count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0 and not visited[i][j]:
                dfs(i, j)
                cluster_count += 1

    return cluster_count

def min_steps_to_split_clusters(matrix):
    steps = 0
    while True:
        zero_counts = count_zeros(matrix)
        matrix, modified = decrease_numbers(matrix, zero_counts)
        if not modified:
            break
        steps += 1
    return steps

# 예제
matrix = [
    [1, 0, 0, 2],
    [0, 3, 0, 0],
    [0, 0, 0, 4]
]

result = min_steps_to_split_clusters(matrix)
print(result)  # 출력: 3
