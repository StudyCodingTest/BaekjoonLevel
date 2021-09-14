# 1로 만들기
# 628ms
cnts = [0,0]
for n in range(2,int(input())+1):
    cnts.append(cnts[n-1]+1)
    if n%3 == 0: cnts[-1] = min(cnts[-1],cnts[n//3]+1)
    if n%2 == 0: cnts[-1] = min(cnts[-1],cnts[n//2]+1)
print(cnts[-1])