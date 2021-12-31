def function(a,b,c):
    if(c <= b):
        return -1
    else :
        return int(a/(c-b)) + 1

a, b, c = map(int, input().split())
print(function(a,b,c))
