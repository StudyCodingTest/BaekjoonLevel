# <heap 구조에 대한 이해>
# min heap: 부모노드가 자식노드보다 작거나 같은 구조
# max heap: 보모노드가 자식노드보다 크거나 같은 구조
# import heapq를 사용하면 자동으로 heap구조를 유지하면서 heap을 사용할 수 있음

# 이 문제는 단순 input()을 사용하면 시간초과가 발생한다.
# 따라서 조금 더 속도가 빠른 sys.stdin.readline()을 사용한다.
import sys
import heapq
sys.stdin = open('input', 'r')

n = int(sys.stdin.readline())
a = []
heapq.heapify(a)
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(a) == 0:
            print(0)
        else:
            print(-heapq.heappop(a))
    else:
        heapq.heappush(a, -num)
