n, m = map(int, input().split())
if m > n//2: m = n - m
numerator, denominator = 1, 1
for i in range(m):
    numerator *= (n-i)
    denominator *= (m-i)
print(numerator//denominator)