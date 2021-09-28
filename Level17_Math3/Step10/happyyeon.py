# 패션왕 신해빈
#

from math import comb
import sys
input = sys.stdin.readline
clothes = {}
for _ in range(int(input())) :
    n = int(input())

    count = 1

    name, type = input().split()

    # 어차피 같은 이름의 옷은 없으니까
    if type in clothes :
        clothes[type] += 1
    else :
        clothes[type] = 1
    
    for i in range(n) :
        count = count*(clothes[i]+1)

print(count-1)