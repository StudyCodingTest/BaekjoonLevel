# 괄호
# 76ms

for _ in range(int(input())) :
    standard = 0 # YES인지 NO인지 판단해주는 기준
    ps = input()

    for i in range(len(ps)) :
        if ps[i] == "(" :
            standard += 1
        elif ps[i] == ")" :
            standard -= 1
        
        if standard < 0 : # )가 (보다 먼저 나온 경우
            print("NO")
            break
    # for 문을 다 돌았을 때
    if standard == 0 :
        print("YES")
    elif standard > 0 :
        print("NO")

