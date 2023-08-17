def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack == []:
                return False
            else:
                stack.pop()
    return True if len(stack) == 0 else False