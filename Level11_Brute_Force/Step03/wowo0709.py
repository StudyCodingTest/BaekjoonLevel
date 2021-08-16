# 덩치
# 76ms
N = int(input())
bulks = []
for i in range(N):
    bulks.append([i]+input().split()) # 번호, 키, 몸무게
# 시간 단축을 위해 정렬 활용
bulks.sort(key=lambda bulk:(bulk[1],bulk[2]), reverse=True)
for i in range(len(bulks)):
    rank = 1
    for j in range(i):
        if bulks[j][1] > bulks[i][1] and bulks[j][2] > bulks[i][2]: rank += 1
    bulks[i].append(rank)
    
print(*[bulk[3] for bulk in sorted(bulks)])