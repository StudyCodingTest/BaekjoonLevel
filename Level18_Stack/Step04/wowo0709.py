# 균형잡힌 세상
# 368ms
while True:
    stack = []
    string = input()
    if string == '.': exit(0)
    for s in string:
        if s == '(' or s == '[': stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(': stack.pop()
            else: break
        elif s == ']':
            if stack and stack[-1] == '[': stack.pop()
            else: break
    else:
        if stack: print('no') # 남는 왼쪽 괄호가 있는 경우
        else: print('yes')        
        continue
    print('no') # 틀린 오른쪽 괄호가 있는 경우