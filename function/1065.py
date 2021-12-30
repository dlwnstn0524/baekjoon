def check_han_num(a) :
    ans = 0
    if len(a) == 1 : #한자리수는 모두 한수로 처리
        ans = 1
    elif len(a) == 2 : #두자리수는 모두 한수로 처리
        ans = 1 
    elif  len(a) == 3 :
        if int(a[0]) + int(a[2]) == 2*int(a[1]) :
            ans = 1
    return ans

n = input()
cnt = 0


for i in range(1, int(n)+1):
    if check_han_num(str(i)) == 1:
        cnt += 1
print(cnt)