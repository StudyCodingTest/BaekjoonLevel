# 후위 표기식
'''
중위표기식 -> 후위표기식
1. 중위표기식을 연산자 우선순위에 따라 괄호로 묶어준다. 
2. 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨준다. 
코드로 짤 때
a-b*c/d abc*d/- abc*d/- 
1. 앞에서부터 차례로 탐색
2-1. 피연산자면 스택에 넣는다. 
2-2. 괄호 또는 연산자면 다른 스택에 넣는다. 
3-1. 뒤에 들어오는 연산자가 이미 있던 연산자보다 높은 우선순위이면 그냥 넣는다. 
3-2. 뒤에 들어오는 연산자가 이미 있던 연산자보다 낮거나 같은 우선순위이면 들어온 연산자보다 낮은 우선순위의 연산자가 나올 때까지 스택에 있던 연산자들을 하나씩 차례로 빼서 피연산자 스택에 넣는다. 
3-3-1. 여는 괄호이면 그대로 넣는다. 
3-3-2. 닫는 괄호이면 여는 괄호가 나올 때까지 스택에 있던 연산자들을 하나씩 차례로 빼서 피연산자 스택에 넣는다. 
4. 수식이 끝나면 연산자 스택에 있던 연산자들을 하나씩 빼서 피연산자 스택에 넣는다.  
'''
s = list(input())
priority = {'+':1, '-':1, '*':2, '/':2}
operands, operators = [], []
for op in s:
    if op.isalpha():
        operands.append(op)
    else:
        if op == '(':
            operators.append(op)
        elif op == ')':
            while operators and operators[-1] != '(':
                operands.append(operators.pop())
            operators.pop() # remove '('
        else:
            while operators and operators[-1] != '(' and priority[operators[-1]] >= priority[op]:
                operands.append(operators.pop())
            operators.append(op)
    print(op, operands, operators)
ans = operands + operators[::-1]
print(''.join(ans))
