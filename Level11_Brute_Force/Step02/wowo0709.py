# 분해합
# 2148ms
N = int(input())
for num in range(N):
    if sum(list(map(int, [str(num)]+list(str(num))))) == N:
        print(num)
        break
else:
    print(0)