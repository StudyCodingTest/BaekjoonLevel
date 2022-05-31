import sys
from collections import deque
sys.stdin = open('input', 'r')
# D개수가 배열의 원소보다 많으면 그냥 바로 error출력하면 된다.

# R: 배열에 있는 수의 순서를 뒤집는다.
#D: 첫번째 수를 버리는 함수, 배열 비어있을 때 사용하면, error출력

t = int(sys.stdin.readline())


# def R(x_list):
#     nx_list = [0] * len(x_list)
#     for i in range(len(x_list)):
#         nx_list[(len(x_list) - i - 1)] = x_list[i]
#     return nx_list
#
#
# def D(x): # D연산을 위한 함수, 어차피 맨 앞의 원소만을 버리기때문에 원소의 개수를 입력받을 필요X
#     if len(x) == 0:
#         # print('error')
#         return 'error'
#     x.pop(0)
#     return x


for _ in range(t):
    operation = sys.stdin.readline()
    n = int(sys.stdin.readline())
    # x = x.replace(',', '')
    # print(x)
    if n > 0:
        x = sys.stdin.readline()[1:-2].split(',')
        x = deque(x)
        # x = deque(map(int, sys.stdin.readline().rstrip()[1:-1].split(',')))
        # print(x)
    elif n == 0:
        x = deque([])

    flag_r = 0
    flag_e = 0

    for i in operation:
        if i == 'R':
            flag_r += 1
        elif i == 'D':
            if len(x) == 0:
                print('error')
                break
            else:
                if flag_r % 2 == 0:
                    x.popleft()
                else:
                    x.pop()

    else:
        if flag_r % 2 == 0:
            print('[' + ','.join(x) + ']')
        else:
            x.reverse()
            print('[' + ','.join(x) + ']')









    # check_r = 0
    # flag_e = 0
    # for i in range(len(operation)):
    #     if check_r == 1: # 만약 check_r flag가 올라가있다면
    #         check_r = 0 # flag를 내려주고 continue
    #         continue
    #     if operation[i] == 'R':
    #         if operation[i+1] == 'R': # 뒤집기 연산이 두번연속나오면 그대로이다.
    #             check_r = 1 # flag를 올려주고 continue
    #             # print('check')
    #             continue
    #         else: # 뒤집기 연산이 연속으로 나오는 것이 아니라면 R연산 수행
    #             x.reverse() # queue의 reverse()를 사용하여 간단하게 구현
    #     elif operation[i] == 'D':
    #         if len(x) == 0: # 버릴 것이 없을 때
    #             # print('error')
    #             flag_e = 1 # error flag를 올려주고 반복문을 빠져 나온다.
    #             break
    #         else: # 버릴 것이 있다면, queue의 popleft()함수를 사용하여 간단하게 구현
    #             x.popleft()
    # if flag_e == 1: # 반복문을 빠져나온 후 error flag가 올라가있다면
    #     print('error') # error 출력
    # else: # error가 발생한 경우가 아니라면 모든 연산이 끝난 후 정답 출력
    #     # print('[' + ','.join(x) + ']')
    #     print(list(x))
    # print(D(x_list))
    # print(R(x_list))

