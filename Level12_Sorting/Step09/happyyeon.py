# 나이순 정렬
# 348ms

import sys

dict_users = dict()
# (나이, 이름) 튜플로 받음 이 때 각각의 키 값은 들어온 순서
for i in range(int(sys.stdin.readline())) :
    age, name = sys.stdin.readline().split()
    dict_users[i+1] = (age,name)

# 나이 순, 들어온 순으로 정렬 (반환값 = 키)
sorting_keys = sorted(dict_users.keys(), key= lambda x : int(dict_users[x][0]))

#결과 출력 (키 --> value)
for key in sorting_keys :
    print(dict_users[key][0], dict_users[key][1])



########## 또 다른 풀이 #############

# import sys
# n = int(sys.stdin.readline())
# member = []
# for i in range(n):
#     member.append(list(sys.stdin.readline().split()))
# member.sort(key=lambda x: int(x[0]))
# for i in range(n):
#     print(member[i][0], member[i][1])


