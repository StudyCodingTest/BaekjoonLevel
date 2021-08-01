# 문자열 반복
# 80ms
for _ in range(int(input())):
    R, S = input().split()
    print(*[s*int(R) for s in S],sep='')