#문제: 정수 N개의 합, 시간: 192ms
def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans


n = 5
a = []
for i in range(1, n+1):
    a.append(i)
print(solve(a))
