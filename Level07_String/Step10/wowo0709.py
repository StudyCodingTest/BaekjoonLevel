# 그룹 단어 체커
# 184ms
from string import ascii_lowercase as asc

answer = 0
for _ in range(int(input())):
    checker = dict(zip(asc,[0 for _ in range(26)]))
    pre = ''
    for w in input():
        if w != pre and checker[w]: break
        checker[w], pre = True, w
    else: answer += 1

print(answer)