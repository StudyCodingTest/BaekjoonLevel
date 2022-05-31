# <기존 방식>
# 팩토리얼 함수를 재귀를 이용하여 구현하였다.
# --> 런타임에러: RecursionError 발생

# <수정된 방식>
# for문을 이용한 단순연산으로 팩토리얼 함수 구현

import sys
sys.stdin = open('input', 'r')


def factorial(n):
    # global ans
    # if n == 1:
    #     # print(ans)
    #     return ans
    # ans *= n
    # factorial(n-1)
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


# ans = 1
num = []
cnt = 0
n = int(input())
ans = factorial(n)
ans = str(ans)
print(ans)

for i in range(len(ans)-1, -1, -1):
    # print(i)
    num.append(ans[i])
# print(num)
for i in num:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)
