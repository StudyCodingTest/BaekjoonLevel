# 주유소
# 180ms

import sys
input = sys.stdin.readline

n = int(input())
distances = list(map(int,input().split()))
prices = list(map(int,input().split()))

min_price = prices[0] # 최소 기름값, 첫 번째 도시에서는 반드시 주유를 해야함
sum_price = min_price*distances[0] # 도시 경유 중 총 기름값

# 최소의 가격으로 많은 거리를 이동해야 한다.
for i in range(1,len(distances)) :
    if prices[i] < min_price : 
        min_price = prices[i]
    sum_price += min_price*distances[i]

print(sum_price)
