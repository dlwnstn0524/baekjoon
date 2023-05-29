n, k = map(int, input().split())

def function(elements, length):
    if length == 0:
        return [[]]

    permutations = []
    for element in elements:
        for sub_permutation in function(elements, length - 1):
            permutations.append([element] + sub_permutation)
    return permutations

elements = []
for i in range(n, 0, -1):
    elements.append(i)
permutations = function(elements, k)


# 중복순열 출력
for permutation in permutations:
    for i in permutation:
        print(i, end=" ")
    print()