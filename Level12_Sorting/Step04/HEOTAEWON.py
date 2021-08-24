#문제: 통계학
#시간: 532ms


import sys
import collections

n = int(sys.stdin.readline())
nums = [] # 숫자들을 저장할 리스트
for _ in range(n): # 숫자들을 하나씩 리스트에 저장
    nums.append(int(sys.stdin.readline()))
nums.sort() # 숫자들을 오름차순으로 정렬

print(round(sum(nums)/len(nums))) # round(): 반올림 함수

print(nums[len(nums)//2])

count = collections.Counter(nums).most_common()
# collections를 import하면 Counter이라는 함수를 사용할 수 있다.
# Counter함수는 해당 값의 빈도 수를 반환해주며 기본으로 dictionary 형태로 반환한다.
# Counter.most_common()의 경우 가장 빈도수가 높은 것을 반환해주며 이 경우에는 튜플로 반환한다.
# 튜플은 (값, 빈도수) 형태로 반환된다.

if len(count) > 1: # 인덱스의 개수가 2개 이상이어야 아래 코드에서 오류가 나지 않는다.
    if count[0][1] == count[1][1]: # 빈도수가 같은 경우 숫자가 두번째로 큰 것을 출력
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])

print(nums[-1]-nums[0])
