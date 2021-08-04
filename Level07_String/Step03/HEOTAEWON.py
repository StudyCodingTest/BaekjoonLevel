#문제: 알파벳 찾기, 시간: 76ms
a = 'baekjoon'
b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

test = dict()
for i in range(len(a)):
    if a[i] in test:
        continue
    test[a[i]] = i
print(test)
for n in b:
    if n in a:
        print(test[n], end=' ')
    else:
        print(-1, end=' ')
