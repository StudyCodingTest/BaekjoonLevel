# 회의실 배정
# 348ms

import sys
from types import coroutine
input = sys.stdin.readline

n = int(input())
refers_table = []
for _ in range(n) :
    refers_table.append(list(map(int,input().split())))

refers_table.sort(key=lambda x:(x[1],x[0])) # y 정렬 -> x 정렬

count = 1
cur_time = refers_table[0][1]
for i in range(1,n) : 
    if refers_table[i][0] >= cur_time : # 시작시간이 현재시간 이후일 때
        count += 1
        cur_time = refers_table[i][1]

print(count)




