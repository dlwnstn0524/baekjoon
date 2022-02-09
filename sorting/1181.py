n = int(input())
words = []
for i in range(n) :
    words.append(input())

words = set(words)
words = list(words)
words.sort()
words.sort(key = len)

for word in words:
    print(word)