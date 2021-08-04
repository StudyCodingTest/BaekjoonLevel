# 문제 : 정수 N개의 합 , 시간 : 40ms
# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성

# 조건
# a : 합을 구해야 하는 정수 n개가 저장되어 있는 리스트
# 리턴값 : a에 포함되어 있는 정수 n개의 합
a = [1,2,3,4,5]

def solve(a):
    ans = sum(a)
    return ans

print(solve(a))