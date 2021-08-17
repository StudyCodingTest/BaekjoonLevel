#문제: 팩토리얼
#번호: 10872
#시간: 80ms


def factorial(n):
    if n == 0: # 0일 경우 1을 반환 (0! = 1)
        return 1
    else:
        return n*factorial(n-1) # 0이 될때까지 1씩 감소하여 factorial 함수를 호출


n = int(input())
print(factorial(n))
