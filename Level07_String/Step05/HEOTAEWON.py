#문제: 단어 공부, 시간: 124ms
import sys


a = sys.stdin.readline()
a = a.upper()
b = list(set(a))
b.sort()
b.pop(0)

test = []
test_max = []
maxnum = 0
for alpha in b:
    test.append(a.count(alpha))

for i in range(len(test)):
    if test[i] > maxnum:
        maxnum = test[i]
        test_max.append(i)

test.sort()
if len(test)>=2 and test[-1] == test[-2]:
    print('?')
else:
    print(b[test_max[-1]])
