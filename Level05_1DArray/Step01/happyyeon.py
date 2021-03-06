# 문제 : 최소 , 최대 , 번호 : 10818, 소요 시간 : 468ms
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을
# 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N(1<= N <= 1,000,000)이 주어진다.
# 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.

# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로
# 구분해 출력한다.

n = int(input()) # N 값 입력 받음
lst = list(map(int, input().split())) # N개의 정수를 입력 받음

print(min(lst), max(lst)) 