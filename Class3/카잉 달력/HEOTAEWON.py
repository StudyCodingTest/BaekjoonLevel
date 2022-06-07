import sys
sys.stdin = open('input', 'r')

t = int(input())


def kiing(m, n, x, y):
    k = x  # x값을 받아온다.
    while k <= m * n:  # k의 범위는 m*n을 넘을 수 없다.
        # x, y는 x에 m만큼 더했을 때 x번째 이동한 해수와
        # y에 n만큼 더했을 때 y번째 이동한 해수가 동일한 경우이다.
        # 따라서 k에서 각각 x, y만큼 뺀 후 m과 n으로 나누었을 때 나머지가 0인경우 반환한다.
        if (k - x) % m == 0 and (k - y) % n == 0:
            return k
        k += m # 아닌 경우 k에 계속 m씩 더해준다.
    return -1 # 해당 조건을 만족하지 못한채 벗어나면 유효하지 않은 경우이므로 -1을 반환한다.

for _ in range(t):
    m, n, x, y = map(int, input().split())

    print(kiing(m, n, x, y))



