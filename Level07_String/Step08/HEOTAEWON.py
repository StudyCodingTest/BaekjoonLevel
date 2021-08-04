#문제: 다이얼, 시간: 72ms
alpha = input()
alpha_list = []
time = 0

for i in alpha:
    alpha_list.append(i)
print(alpha_list)

for n in range(len(alpha_list)):
    if 65<= ord(alpha_list[n]) < 68:
        alpha_list[n] = 2
    elif 68 <= ord(alpha_list[n]) < 71:
        alpha_list[n] = 3
    elif 71 <= ord(alpha_list[n]) < 74:
        alpha_list[n] = 4
    elif 74 <= ord(alpha_list[n]) < 77:
        alpha_list[n] = 5
    elif 77 <= ord(alpha_list[n]) < 80:
        alpha_list[n] = 6
    elif 80 <= ord(alpha_list[n]) < 84:
        alpha_list[n] = 7
    elif 84 <= ord(alpha_list[n]) < 87:
        alpha_list[n] = 8
    else:
        alpha_list[n] = 9
print(alpha_list)
for add_time in alpha_list:
    time += (add_time+1)
print(time)
