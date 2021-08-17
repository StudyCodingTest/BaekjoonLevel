#문제: 블랙잭
#번호: 2798
#시간: 500ms


import sys


def blackjack(m, nums): #m과 카드에 적힌 수들을 리스트로 입력받음
    max_num = 0 # 숫자들의 합을 저장할 변수
    for x in range(len(nums)):
        for y in range(len(nums)):
            if y == x: # 같은 카드를 뽑는 경우 제외
                continue
            for z in range(len(nums)):
                if x == z or y == z: # 같은 카드를 뽑는 경우 제외
                    continue
                elif (nums[x] + nums[y] + nums[z]) > m: # m보다 커지는 경우 제외
                    continue
                max_num = max(max_num, (nums[x] + nums[y] + nums[z])) # 각 카드의 숫자를 더한 것 중 더 큰 값을 선택
    return max_num


n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
print(blackjack(m, nums))

## 3장을 뽑으므로 for문을 3번 이용하여 모든 경우의 수를 확인하였다.
