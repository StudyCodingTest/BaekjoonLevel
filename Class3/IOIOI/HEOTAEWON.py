import sys
sys.stdin = open('input', 'r')

n = int(input())
m = int(input())
s = input()

ans, index, cnt = 0, 0, 0

while index < m-1: #index 범위를 벗어나면 반복문 탈출
    if s[index:index+3] == 'IOI': # 만약 ioi가 발견된다면
        cnt += 1 # cnt를 하나 올려준다.

        if cnt == n: # ioi를 발견하고 cnt를 1 증가하였을 때 n과 동일해진다면 p가 발견된 것이다.
            ans += 1 # 이 경우 p의 발견횟수를 1 증가시킨다.
            cnt -= 1 # 또한, cnt를 1 감소해준다. 왜냐하면 이어서 또 p가 나올 수 있기 때문이다.
        index += 1 # 만약 ioi가 발견되었지만 아직 n만큼 발견되지 않았다면 index를 1증가해준다.
    else: # 발견되지 않은 경우 cnt를 0으로 초기화해준다.
        cnt = 0
    index += 1 # ioi가 발견되지 않은 경우에는 다음 index를 검사하고 발견된 경우에는 index를 하나 더 증가하여 다음 i부터 검사한다.

print(ans)
