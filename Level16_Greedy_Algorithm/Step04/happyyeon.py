# 잃어버린 괄호
# 72ms
import sys
input = sys.stdin.readline
equation = input() # 55-50+40
if "-" not in list(equation) : # 식에 -가 없는 경우 고려
        print(eval(equation))
else :
    for i in range(len(equation)) :
        
        if equation[i] == "-" : # 최초의 -가 발견되면 그 이후는 전부 - 리스트에 집어 넣는다.
            nums_plus = list(map(int,equation[:i].split("+"))) # +
            nums_minus = list(map(int,equation[i+1:].replace("-","+").split("+"))) #-
            break
    print(sum(nums_plus) - sum(nums_minus))


