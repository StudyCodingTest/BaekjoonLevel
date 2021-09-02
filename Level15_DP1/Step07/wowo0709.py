# 계단 오르기
# 76ms
# 전계단 안 밟은 최대 점수, 전계단 밟은 최대 점수
stairs = [[0,0]]+[[int(input())]*2 for _ in range(int(input()))]
for i in range(2,len(stairs)):
    stairs[i][0] += max(stairs[i-2])
    stairs[i][1] += stairs[i-1][0]
print(max(stairs[-1]))

