#문제: 골드바흐의 추측
#번호: 9020
#시간: 1948ms


import sys


all_nums = list(range(1, 10001)) # 범위만큼 소수를 만들어줌
nums_sosu = [] # 소수를 저장할 리스트
# 범위 내 소수들만 추가
for n in all_nums:
    if n == 1:
        continue
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            break
    else:
        nums_sosu.append(n)

for _ in range(int(sys.stdin.readline())): # testcase만큼 반복
    num = int(sys.stdin.readline()) # 숫자를 입력받음

    middle_1 = num//2 # 가운데에서부터 시작

    for i in range(len(nums_sosu)):
        # 가운데에서부터 소수이며 뺀 값도 소수이면 출력
        if middle_1 in nums_sosu and num-middle_1 in nums_sosu:
            print(num-middle_1, middle_1)
            break
        # 아닐경우 1씩 증가
        else:
            middle_1 += 1
