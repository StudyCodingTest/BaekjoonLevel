import sys
input = sys.stdin.readline
print = sys.stdout.write
N, M = map(int, input().split())
pok_dict = dict()
for e, _ in enumerate(range(N)):
    name = input().rstrip()
    pok_dict[name] = str(e+1)
    pok_dict[str(e+1)] = name
for _ in range(M):
    print(pok_dict[input().rstrip()]+'\n')