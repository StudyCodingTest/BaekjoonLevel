#문제: 베르트랑 공준
#번호: 4948
#시간:

nums = [] #input 숫자들을 저장할 리스트
while True: #0이 들어올때까지 리스트에 숫자들 저장
    num = int(input())
    if num == 0:
        break
    nums.append(num)
for n in nums: #리스트에 있는 숫자들을 하나씩 검사
    nums_sosu = [] #소수들을 저장할 리스트
    for i in range(n+1, n*2 + 1): #입력받은 소수의
        if i == 1:
            continue
        for x in range(2, int(i**0.5)+1):
            if i%x == 0:
                break
        else:
            nums_sosu.append(i)
    print(len(nums_sosu))
