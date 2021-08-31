# 파도반 수열
# 80ms
import sys
input = sys.stdin.readline
array_pn = [0] * 101 # 수열 memoization
for _ in range(int(input())) :
    n = int(input())
    array_pn[1],array_pn[2],array_pn[3],array_pn[4],array_pn[5] = 1,1,1,2,2 # DP 초기값

    for num in range(6,n+1) : # 규칙성 발견(1,1,1,2,2,3,4,5,7,9,12,16,21,28,37,...)
        array_pn[num] = array_pn[num-1] + array_pn[num-5]

    print(array_pn[n])
