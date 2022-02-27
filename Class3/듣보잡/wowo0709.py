N, M = map(int, input().split())
dbj_dict = dict()
for _ in range(N):
    dbj_dict[input()] = 1
ans = []
for _ in range(M):
    name = input()
    if name in dbj_dict:
        ans.append(name)
print(len(ans), *sorted(ans), sep='\n')