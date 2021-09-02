# 정수 삼각형
#

import sys
input = sys.stdin.readline

n = int(input())
layers = [] # 삼각형의 한 층
for _ in range(n) : # 층층이 추가
    layers.append(list(map(n,input().split())))

for layer in range(1,n) : # 층 수
    for location in range(layer+1) : # 해당 층의 위치
        # 첫 번째와 마지막 값은 길이 하나 밖에 없음
        if location == 0 :
            layers[layer][location] += layers[layer-1][location]
        elif location == layer :
            layers[layer][location] += layers[layer-1][location-1]
        # 나머지 값들은 지금까지의 누적합들 중에서 최선을 따라 가면 됨
        else :
            layers[layer][location] += max(layers[layer-1][location-1],layers[layer-1][location])
        
print(max(layers[n-1]))

