# 균형잡힌 세상
# 140ms

import sys
input = sys.stdin.readline

while True :
    string = input().rstrip() # 오른쪽 공백 제거 
    if string == "." : # 종료 조건
        break
    flag = True # yes or no 판단 기준
    stack = []

    for i in range(len(string)) :
        if string[i] == "[" or string[i] == "(" : # 여는 괄호면 stack에 push
            stack.append(string[i])
        elif string[i] == "]" or string[i] == ")" : # 닫는 괄호 
            if not stack : # 빈 스택이면 서로 같지 않은 문자열
                flag = False
                break
            elif string[i] == "]" and stack[-1] == "[" : # 마지막 여는 괄호와 일치하면 pop
                stack.pop()
            elif string[i] == ")" and stack[-1] == "(" : 
                stack.pop()
            else :
                flag = False
                break
    # 판단 기준  = O & 빈 스택(for 문을 정상적으로 종료하였을 때)
    if flag and not stack :
        print("yes")
    else :
        print("no")
            
        
