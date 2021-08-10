# 문제 : 숫자의 개수, 문제 번호 : 2577 , 소요 시간 : 72ms
# 세 개의 자연수 A,B,C가 주어질 때 A X B X C를 계산한 결과에
# 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하시오.

# 입력
# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다.
# A,B,C는 모두 100보다 크거나 같고, 1000보다 작은 자연수

# 출력
# 첫째 줄에는 A X B X C의 결과에 0이 몇번 쓰였는지
# 마찬가지로 둘째 줄부터 열 번째 줄까지 AXBXC의 결과에
# 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 하나씩 출력

# A,B,C 입력 받음
a = int(input())
b = int(input())
c = int(input()) 
currentNumber = a * b * c # 현재 숫자 초기화
lst = []

while currentNumber != 0 : # 몫과 나머지가 둘 다 0이 될 때 까지 
    x, y = divmod(currentNumber, 10) 
    # temp = (currentNumber) // 10 # 10으로 나눈 몫
    lst.append(y) # 10으로 나눈 나머지를 리스트에 추가
    currentNumber = x

for i in range(10) : #0~9 까지
    print(lst.count(i)) # 리스트 내에서 i의 개수가 몇 개인지 출력 

