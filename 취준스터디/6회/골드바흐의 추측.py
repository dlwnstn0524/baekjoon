# prime_list는 1부터 10000사이의 소수가 오름차순으로 저장된 리스트예요.
from prime import prime_list

def check(target):
    for i in prime_list:
        if i > target // 2 :
            break
        else:
            if target - i in prime_list:
                answer = [i, target - i]
    return answer


# 합계가 짝수가 되는 두 소수를 찾는 함수예요.
def goldbach(arr):
    # 합계가 짝수가 되는 두 소수를 작은 수부터 차례로 리스트에 저장해 주세요.
    answer = []
    for i in arr:
        answer.append(check(i))
    return answer


arr = [int(x) for x in input().split()]

for i in goldbach(arr):
    print(i[0], i[1])
