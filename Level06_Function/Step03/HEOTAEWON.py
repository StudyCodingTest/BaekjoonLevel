#문제: 한수, 시간: 76ms
def solve(n):
    global count
    if(1<= n <100):
        count += 1
    elif(100<= n < 1000):
        a, b = divmod(n, 100)
        c, d = divmod(b, 10)
        if(a-c == c-d):
            count += 1
    elif(n == 1000):
        a, b = divmod(n, 1000)
        c, d = divmod(b, 100)
        e, f = divmod(d, 10)
        if(a-c == c-e == e-f):
            count += 1


count = 0
a = 1000
for i in range(1, a+1):
    solve(i)
print(count)
