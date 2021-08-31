# 신나는 함수 실행
# 1256ms
def w(a,b,c):
    if (a,b,c) in ws:
        return ws[(a,b,c)]
    elif a <= 0 or b <= 0 or c <= 0:
        ws[(a,b,c)] = 1
    elif a > 20 or b > 20 or c > 20:
        ws[(a,b,c)] = w(20,20,20)
    elif a < b < c:
        ws[(a,b,c)] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        ws[(a,b,c)] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    
    return ws[(a,b,c)]

ws = dict()
while True:
    a,b,c = map(int, input().split())
    if a == b == c == -1: exit(0)
    print("w({0}, {1}, {2}) = {3}".format(a,b,c,w(a,b,c)))


