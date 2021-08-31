import sys

dict_users = dict() # 회원 정보

# 회원 정보 입력 받음 , (이름, 나이)
for i in range(int(sys.stdin.readline())) :
    age, name = sys.stdin.readline().split()
    dict_users[name] = int(age)

# 나이 순으로 정렬
list_users = sorted(dict_users.items(), key=(lambda x : x[1]))

#결과 출력
for user in list_users :
    print(user[1], user[0])


