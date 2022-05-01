import sys
input = sys.stdin.readline

# input을 받는다.
equation = input()
answer = "" # 최종 정답 
stack = []
# 입력받은 문자열을 한 글자씩 순회하며 검사한다.
for letter in equation:
    # 알파벳이면 답에 추가
    if letter.isalpha():
        answer += letter
    
    # 우선순위1. 소괄호
    if letter == "(":
        stack.append(letter)
    
    # 우선순위2. *,/
    if letter == "*" or letter == "/":
        while stack and stack[-1] != "(" and (stack[-1] == "*" or stack[-1] == "/"): # 우선순위1에 위배되지 않고 같은 등급의 우선순위2가 쌓였을 때 
            answer += stack.pop()
        stack.append(letter)
    
    # 우선순위3. +,-
    if letter == "+" or letter == "-":
        while stack and stack[-1] != "(": # 우선순위1,2에 위배되지 않고 우선순위3이 쌓였을 때
            answer += stack.pop()
        stack.append(letter)
    
    if letter == ")":
        while stack[-1] != "(":
            answer += stack.pop()
        stack.pop()

# 스택에 남은 거 다 비워냄
while stack:
    answer += stack.pop()

print(answer)
