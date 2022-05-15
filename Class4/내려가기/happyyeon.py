import sys
input = sys.stdin.readline

# 초기 조건
n = int(input()) 
before_a,before_b,before_c = map(int,input().split())
# dp 배열 생성
dp_max = [before_a,before_b,before_c] 
dp_min = [before_a,before_b,before_c]

#dp_max[n] = n행까지의 최대
#dp_min[n]= n행까지의 최소
for i in range(1, n):
    a,b,c = map(int,input().split()) 
    dp_max = [max(dp_max[0], dp_max[1]) + a,max(dp_max[0], dp_max[1], dp_max[2]) + b,max(dp_max[1], dp_max[2]) + c] 
    dp_min = [min(dp_min[0], dp_min[1]) + a,min(dp_min[0], dp_min[1], dp_min[2]) + b,min(dp_min[1], dp_min[2]) + c] 

print(max(dp_max), min(dp_min))




