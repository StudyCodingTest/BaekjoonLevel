#문제: 숫자의 합, 시간: 72ms
count = 11
num = 10987654321
ans = []

while count>0:
    a, b = divmod(num, 10)
    ans.append(b)
    num = a
    count -= 1
print(sum(ans))
