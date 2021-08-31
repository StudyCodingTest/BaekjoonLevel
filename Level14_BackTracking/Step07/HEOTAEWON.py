#문제: 연산자 끼워넣기
#시간: 108ms


import sys


def calculate(num, nums_index, plus, minus, multi, divide): # 계산값, 인덱스 번호, 각 연산들을 입력으로 받음
    global ans_max, ans_min # global로 선언하는 경우 전역변수로 어디서나 통용되도록 사용할 수 있음
    if nums_index == n: # 인덱스 번호가 숫자의 개수와 같아지는 경우 연산이 끝난 것이므로 결과를 반환함
        ans_max = max(ans_max, num) # 최대값
        ans_min = min(ans_min, num) # 최소값
        return

    if plus > 0: # plus 변수가 아직 남아있는 경우
        # plus 연산을 해준 값을 입력으로 넣고 index 1증가, plus 1감소된 값을 입력으로 재귀실행
        calculate(num+nums[nums_index], nums_index+1, plus-1, minus, multi, divide)
    if minus > 0: # minus 변수가 아직 남아있는 경우
        # minus 연산을 해준 값, index 1증가, minus 1 감소된 값을 입력으로 재귀실행
        calculate(num-nums[nums_index], nums_index+1, plus, minus-1, multi, divide)
    if multi > 0: # multi 변수가 아직 남아있는 경우
        # 곱하기 연산을 해준 값, index 1증가, multi 1감소된 값을 입력으로 재귀실행
        calculate(num * nums[nums_index], nums_index+1, plus, minus, multi-1, divide)
    if divide > 0: # divide 변수가 아직 남아있는 경우
        if num < 0: # 만약 입력이 음수인 경우 양수로 변환해준 뒤 몫을 취하고 다시 음수로 변환해줌
            calculate(-(-num//nums[nums_index]), nums_index+1, plus, minus, multi, divide-1)
        else:
            calculate(num//nums[nums_index], nums_index+1, plus, minus, multi, divide-1)


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split())) # 입력을 정수형, 리스트로 한번에 저장
plus, minus, multi, divide = map(int, sys.stdin.readline().split())
ans_max, ans_min = -1e9, 1e9 # 각각 -10억, 10억
calculate(nums[0], 1, plus, minus, multi, divide) # 첫번째 숫자를 입력으로, 따라서 인덱스는 그 다음인 1로 시작
print(ans_max)
print(ans_min)

## num 변수를 각 if문 별로 계산을 해준뒤 함수의 입력으로 넣어주는 경우 해결되지않았다.
# 원인은 변수 자체를 바꾼다음 함수를 실행할 경우 코드 상 뒤에 위치하는 연산들이 실행될 때 영향을 미치기 때문이다.
# 예를 들어 3+4 연산이 먼저 실행된 후 한가지 경우의 연산을 실행 했을때
# 후에 3*4 연산이 먼저 실행되는 경우를 계산할 때 올바른 값이 입력으로 들어가지 않는다.
# 따라서 함수 자체의 입력을 계산하여 재귀를 실행하여야 한다.
