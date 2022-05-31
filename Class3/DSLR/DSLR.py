import sys
from collections import deque
sys.stdin = open('input', 'r')

# visited를 list로 만들어 사용하였다. 하지만, 이 경우 in을 이용한 탐색을 사용하면 O(n)의 시간복잡도
# But, set으로 만들어 in 탐색을 하면 시간 복잡도가 O(1)이다.
# 따라서 순서에 관계없이 원소의 단순 포함 유무만 체크한다면, set을 이용하는게 더 유리하다.
# visited의 목록에서 원소포함 여부를 확인하여 연산 --> 시간초과
# visited에 해당 숫자만큼 인덱스를 만들어 True, False로 구분하여 경로 저장 --> 시간초과
# DSLR 각각 함수로 만들어 사용하여 연산 적용 --> 시간초과
# 바로 즉시 연산하여 queue에 삽입 --> 시간초과
# 아직 해결하지 못함


# def D(n):
#     n *= 2
#     if n > 9999:
#         n %= 10000
#     return n
#
#
# def S(n):
#     n -= 1
#     if n < 0:
#         return 9999
#     return n
#
#
# def L(n):
#     d1 = n // 1000
#     d2d3d4 = n % 1000
#     n = d2d3d4 * 10 + d1
#     return n
#
#
# def R(n):
#     d4 = n % 10
#     d1d2d3 = n // 10
#     n = d4 * 1000 + d1d2d3
#     return n


def DSLR(a, b):
    q = deque()
    visited = [False] * 10000
    q.append((a, ''))
    visited[a] = True
    while q:
        num, operation = q.popleft()

        if num == b:
            print(operation)
            return

        #num_after = D(num)
        num_d = num * 2 % 10000
        if num_d == b:
            print(operation + 'D')
            return
        if not visited[num_d]:
            visited[num_d] = True
            q.append((num_d, operation + 'D'))


        #num_after = S(num)
        num_s = (num - 1) % 10000
        if num_s == b:
            print(operation + 'S')
            return
        if not visited[num_s]:
            visited[num_s] = True
            q.append((num_s, operation + 'S'))

        #num_after = L(num)
        num_l = num % 1000 * 10 + num // 1000
        if num_l == b:
            print(operation + 'L')
            return
        if not visited[num_l]:
            visited[num_l] = True
            q.append((num_l, operation + 'L'))

        #num_after = R(num)
        num_r = num % 10 * 1000 + num // 10
        if num_r == b:
            print(operation + 'R')
            return
        if not visited[num_r]:
            visited[num_r] = True
            q.append((num_r, operation + 'R'))


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    DSLR(A, B)
