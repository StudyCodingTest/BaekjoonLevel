#문제: 상수, 시간: 84ms
a, b = input().split()
a_list = []
b_list = []
for i in range(3):
    a_list.append(a[2-i])
    b_list.append(b[2-i])
for i in range(3):
    if a_list[i] > b_list[i]:
        for n in range(3):
            print(a_list[n], end='')
        break
    elif a_list[i] == b_list[i]:
        continue
    else:
        for m in range(3):
            print(b_list[m], end='')
        break
