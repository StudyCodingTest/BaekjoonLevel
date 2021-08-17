#문제: 수 정렬하기
#번호: 2750
#시간: 120ms


nums = [] # 입력받은 수를 저장할 리스트
for i in range(int(input())): # 입력받은 숫자만큼 수를 입력받은 후 리스트에 저장
    nums.append(int(input()))

nums.sort() # 오름차순 정렬
for n in nums: # 출력
    print(n)
