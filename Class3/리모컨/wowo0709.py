cur_ch, goal_ch = 100, int(input())
imp_nums = []
if int(input()) != 0:
    imp_nums = list(input().split())
pos_nums = [str(i) for i in range(10) if str(i) not in imp_nums]

ans = abs(cur_ch-goal_ch) # 현재 채널에서 숫자 버튼 없이 이동만 하는 경우
from itertools import product as PI
for n in range(1,7):
    if ans <= n: continue
    for case in PI(pos_nums,repeat=n):
        ch = int(''.join(case))
        ans = min(ans,n+abs(ch-goal_ch))
        if ans <= 1: break
print(ans)