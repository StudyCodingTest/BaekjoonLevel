from collections import deque

for _ in range(int(input())):
    command = input()
    num = int(input())
    integer_arr = input()[1:-1].split(",")

    rev,front,back = 0,0,0

    for i in command:
        if i == "R": # 명령어 = R
            rev += 1
        elif rev % 2 == 0: # 명령어 = D 
            front += 1
        else:
            back += 1

    # Error 조건    
    if front+back > num:
        print("error")
    else:
        integer_arr = integer_arr[front:num-back] # D 명령어 수행
    
        # R 명령어 수행
        if rev % 2 == 0:
            print("["+",".join(integer_arr)+"]")
        else:
            print("["+",".join(integer_arr[::-1])+"]")
    



    




