# 문제: 셀프 넘버
# 시간: 76ma
def find_self_number(n):
    return n + sum(map(int,list(str(n))))

answer = [0 for _ in range(10001)]
for n in range(1,10001):
    try: answer[find_self_number(n)] = True
    except: continue

print(*[n for n in range(1,10001) if answer[n] == False],sep='\n') 