# <공통 풀이방식>
# bfs를 이용한다.
# 3가지 연산을 수행한 경우를 너비우선탐색하여 해당위치까지 도달하는 최단시간을 출력

import sys
from collections import deque
sys.stdin = open('input', 'r')

n, k = map(int, input().split())
q = deque()
# q.append((n, 0))
q.append(n)
max_point = 100000
visited = [0] * (max_point + 1)

# <수정된 풀이>
# visited list를 생성하여 해당 위치에 간적이 있는지 확인
# 이 경우 메모리초과가 발생하지 않음

while q:
    nn = q.popleft()
    if nn == k:
        print(visited[nn])
        break
    # 이렇게 하면 if문을 굳이 3번 수행할 필요 없다.
    for i in (nn + 1, nn - 1, nn * 2):
        if 0 <= i <= max_point and visited[i] == 0:
            visited[i] = visited[nn] + 1
            q.append(i)




# <기존 풀이>
# queue 내에 tuple형식으로 (위치, 일 수)를 저장한다.
# 이 경우 메모리초과가 발생한다.
# 정확한 원인은 모르겠지만, 예상되는 원인은
# 방문한적 있는 위치가 중복되는 경우까지 모두 저장하기때문이라고 생각한다.


# while q:
#     nn, day = q.popleft()
#     if nn == k:
#         print(day)
#         break
#     if nn + 1 == k and nn + 1 <= max_point:
#         print(day+1)
#         break
#     elif nn - 1 == k:
#         print(day + 1)
#         break
#     elif nn * 2 == k and nn * 2 <= max_point:
#         print(day+1)
#         break
#     elif nn + 1 <= max_point and nn * 2 <= max_point:
#         q.append((nn+1, day+1))
#         q.append((nn-1, day+1))
#         q.append((nn*2, day+1))

