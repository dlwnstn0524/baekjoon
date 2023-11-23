from itertools import permutations

def solution(numbers):
    answer = []
    numbers_list = []
    for i in numbers:
        numbers_list.append(i)
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers_list, i):
            number = ''.join(j)
            number = int(number)
            if number < 2:
                continue
            
            flag = False
            for j in range(2,int(number**0.5)+1):
                if number%j == 0:
                    flag = True
                    break
            if not flag:
                answer.append(number)
    print(answer)
    return len(set(answer))