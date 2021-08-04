# 벌집
# 80ms
N = int(input())
maxnum = 1 # 해당 라인의 최대수
d = 1      # 거리
while True:
    if N <= maxnum: 
        print(d)
        break
    maxnum += 6 * d
    d += 1