#문제: 셀프 넘버, 시간: 92ms
def d(n):
    if (n<10):
        a ,b = divmod(n, 10)
        ans = n + a + b
    elif (10<= n < 100):
        a, b = divmod(n, 100)
        c, d = divmod(b, 10)
        ans = n + a + c + d
    elif (100<=  n < 1000):
        a, b = divmod(n, 1000)
        c, d = divmod(b, 100)
        e, f = divmod(d, 10)
        ans = n + a + c + e + f
    elif (1000<= n <= 10000):
        a, b = divmod(n, 10000)
        c, d = divmod(b, 1000)
        e, f = divmod(d, 100)
        g, h = divmod(f, 10)
        ans = n + a + c + e + g + h

    return ans


num = set()
num_ = set()

for i in range(1, 10001):
    num.add(i)
for m in range(1, 10000):
    num_.add(d(m))

ans_set = sorted(num.difference(num_))
for x in ans_set:
    print(x)
