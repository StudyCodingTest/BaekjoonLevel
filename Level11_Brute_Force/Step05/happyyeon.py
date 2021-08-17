# 영화감독 숌
# 984ms

import sys

n = int(sys.stdin.readline())
count = 0
start_num = 666

while True :
    if "666" in str(start_num) :
        count += 1
    if count == n :
        print(start_num)
        break
    
    start_num += 1
