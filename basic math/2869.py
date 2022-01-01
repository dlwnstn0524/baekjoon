import math

def function(a, b, v):
    return math.ceil((v-b)/(a-b))

a, b, v = map(int, input().split())
print(function(a,b,v))