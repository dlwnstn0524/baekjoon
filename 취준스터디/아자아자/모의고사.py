def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    correct = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            correct[0] += 1
        if answers[i] == two[i%len(two)]:
            correct[1] += 1
        if answers[i] == three[i%len(three)]:
            correct[2] += 1
    M = max(correct)
    for i in range(3):
        if correct[i] == M:
            answer.append(i+1)
    return answer