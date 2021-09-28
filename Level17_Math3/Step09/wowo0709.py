# 다리 놓기
# 104ms
fact = [1 for _ in range(30)]
for i in range(2,30): fact[i] = i * fact[i-1]

for t in range(int(input())):
    n, m = map(int, input().split())
    print(fact[m]//(fact[m-n]*fact[n]))