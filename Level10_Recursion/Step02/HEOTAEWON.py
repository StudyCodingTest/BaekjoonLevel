#문제: 피보나치 수 5
#번호: 10870
#시간: 84ms


def fibonachi(n):
    if n == 0: #피보나치 수열의 처음은 0으로 시작
        return 0
    elif n == 1: #피보나치 수열의 두번째는 1로 시작
        return 1
    elif n >= 2: #피보나치 수열의 세번째부터는 앞의 두 숫자를 더한 것
        return fibonachi(n-1) + fibonachi(n-2)



n = int(input())
print(fibonachi(n))
