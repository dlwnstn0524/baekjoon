def count_all(n, s):

    if n < 8:
        return 1
    if s.startswith("longlong"):
        return count_all(n-4, s[4:]) + count_all(n-8, s[8:])
    else:
        return count_all(n-1, s[1:])


n = int(input())
s = input()

print(count_all(n, s))