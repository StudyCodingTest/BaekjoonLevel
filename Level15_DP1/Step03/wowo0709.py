# 01타일
# 264ms
a, b = 0, 1
N = int(input())
for n in range(N):
    a, b = b, (a+b) % 15746
print(b)


