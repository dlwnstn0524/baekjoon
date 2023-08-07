def solution(nums):
    answer = 0
    n = len(nums)
    nums = set(nums)
    if len(nums) <= n / 2:
        answer = len(nums)
    else :
        answer = n/2
    return answer