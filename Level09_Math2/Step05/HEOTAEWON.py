#문제: 베르트랑 공준
#번호: 4948
#시간: 2444ms


import sys


nums = list(range(2, 246912)) #input 숫자들을 저장할 리스트
nums_sosu = []

for n in nums: #범위에 있는 숫자들을 하나씩 검사
    if n == 1:
        continue
    for x in range(2, int(n**0.5)+1):
        if n%x == 0:
            break
    else:
            nums_sosu.append(n) # 소수인경우 소수리스트에 추가
num_input = int(sys.stdin.readline()) #첫번째 숫자 입력받음

while num_input != 0: # 입력으로 0이 들어올때까지 반복
    count = 0 # 범위 내에 소수의 개수를 카운트하기위한 변수
    for i in range(len(nums_sosu)): # 소수 리스트만큼 반복
        if num_input < nums_sosu[i] <= num_input*2: # 입력받은만큼에 해당하는 범위 내에 있는 경우 1씩 카운트
            count += 1
    print(count)
    num_input = int(sys.stdin.readline()) # 새로운 숫자를 입력받음
