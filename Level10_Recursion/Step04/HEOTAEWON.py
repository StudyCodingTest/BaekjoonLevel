#문제: 하노이 탑 이동 순서
#번호: 11729
#시간: 1584ms


def hanoi(disks, src, dst, extra): # 원판 수, 시작, 목적지, 여분 (각 기둥을 의미)
    if disks == 1: # 원판 수가 한개라면 그냥 바로 이동(base case)
        hanoi.count += 1 # 이동 횟수 count
        hanoi.moves.append((src, dst))
    else: # 원판 수 1개 이상인 경우
        hanoi(disks-1, src, extra, dst)
        hanoi.count += 1
        hanoi.moves.append((src, dst))
        hanoi(disks-1, extra, dst, src)


hanoi.count = 0 # 이동횟수
hanoi.moves = [] # 이동 경로를 저장할 리스트
disks = int(input())
hanoi(disks, 1, 3, 2) # 1, 3, 2는 항상 고정
print(hanoi.count) # 첫째줄에 이동횟수 출력
for i in range(len(hanoi.moves)): # 이동경로 출력
    print(hanoi.moves[i][0], hanoi.moves[i][1], sep=' ')

## 원판의 수가 2개 이상인 경우 basecase로 breakdown 한다.
# 마지막 basecase가 될 때까지 원판을 extra로 보낸 후
# basecase가 되면 맨 밑에꺼부터 차례대로 dst로 쌓는다.
# 그런 다음 extra를 src로, src를 extra로 생각하여 다시 breakdown 시켜 dst로 원판을 옮긴다.
