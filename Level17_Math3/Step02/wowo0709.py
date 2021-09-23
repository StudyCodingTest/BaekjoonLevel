# 약수
# 80ms
N, factors = int(input()), sorted(list(map(int,input().split())))
print(factors[0]*factors[-1])