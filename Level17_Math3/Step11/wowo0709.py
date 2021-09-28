# 팩토리얼 0의 개수
# 80ms
N = int(input())
ans = [0,0] # two, five
for i in range(2,N+1):
    while True:
        if i % 2 == 0: 
            i //= 2
            ans[0] += 1
        elif i % 5 == 0:
            i //= 5
            ans[1] += 1
        else:
            break
            
print(min(ans))