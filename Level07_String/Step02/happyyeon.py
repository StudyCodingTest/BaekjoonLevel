# 문제 이름 : 숫자의 합
# 문제 번호 : 11720
# 소요 시간 : 80ms

n = int(input()) # N 입력 받음
number = input() # 숫자를 입력 받음 string 형태로
sum = 0 # 숫자의 합 초기화
for i in range(n) : # 인덱스 0 ~ N-1 까지
    sum += int(number[i]) # 숫자를 더함

print(sum) # 숫자 총합 출력