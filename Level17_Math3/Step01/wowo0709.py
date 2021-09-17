# 배수와 약수
# 72ms
while True:
    a, b = map(int, input().split())
    if a == b == 0: exit(0)
    if b % a == 0: print('factor')
    elif a % b == 0: print('multiple')
    else: print('neither')