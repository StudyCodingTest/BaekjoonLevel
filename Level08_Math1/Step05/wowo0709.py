# ACM 호텔
# 84ms
for _ in range(int(input())):
    h, w, n = map(int, input().split())
    q,r = divmod(n, h)
    if r == 0: print(str(h) + str(q).zfill(2))
    else: print(str(r) + str(q+1).zfill(2))