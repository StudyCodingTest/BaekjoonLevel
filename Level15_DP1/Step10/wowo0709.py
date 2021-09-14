# 포도주 시식
# 492ms
wines = [[0,0]] + [[int(input())]*2 for _ in range(int(input()))]
maxScoreX, maxScoreO = 0,0
for i in range(2,len(wines)):
    maxScoreX, maxScoreO = max(maxScoreX,wines[i-2][0]),max(maxScoreO,wines[i-2][1])
    wines[i][0] += max(maxScoreX,maxScoreO)
    wines[i][1] += wines[i-1][0]
print(max(wines[-2]+wines[-1]))

'''
점수 |  0  6  10  13   9   8   1
전 X |  0  6  10  19  25  31  29
전 O |  0  6  16  23  28  33  32
'''