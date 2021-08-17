# 분해합
#

import sys

decomposition = int(sys.stdin.readline()) # 인풋, 분해수

# 분해합 찾기
def get_decomposition(creator) :
    return creator + sum(map(int,list(str(creator))))

creator = decomposition - 9 * len(str(decomposition))# 브루트포스 알고리즘 시작 숫자 

# Value Error 방지
if creator < 1 :
    creator = 1

while True :
    if get_decomposition(creator) == decomposition : # 생성자의 분해합 = 인풋
        print(creator)
        break
    if creator >= decomposition :
        print(0)
        break
    
    creator += 1