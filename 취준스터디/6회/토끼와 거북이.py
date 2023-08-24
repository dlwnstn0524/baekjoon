# 토끼와 거북이가 처음으로 동시에 쉬는 시간을 구해서 출력해 주세요.
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a * b // gcd(a,b)

n, m = map(int, input().split())
print(lcm(n,m))