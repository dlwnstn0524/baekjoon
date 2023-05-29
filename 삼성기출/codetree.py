# n, k = map(int, input().split())

# def function(elements, length):
#     if length == 0:
#         return [[]]

#     permutations = []
#     for element in elements:
#         for sub_permutation in function(elements, length - 1):
#             permutations.append([element] + sub_permutation)
#     return permutations

# elements = []
# for i in range(n, 0, -1):
#     elements.append(i)
# permutations = function(elements, k)


# # 중복순열 출력
# for permutation in permutations:
#     for i in permutation:
#         print(i, end=" ")
#     print()

n, k = map(int, input().split())

def function(arr, len):
    if len == 0 :
        return [[]]
    set = []
    for element in arr :
        for sub_set in function(arr, len-1):
            set.append([element] + sub_set)
    return set

arr = []
for i in range(1, n+1):
    arr.append(i)
answer = function(arr, k)
answer.sort(reverse=True)
for i in answer :
    for j in range(k):
        print(i[j], end=" ")
    print()