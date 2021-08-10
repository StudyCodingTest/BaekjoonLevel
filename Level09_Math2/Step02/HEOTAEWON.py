#문제: 소수
#번호: 2581
#시간: 684ms

M = int(input())
N = int(input())
num_sosu = [] #소수들을 저장할 리스트
for i in range(M, N+1): #M부터 N까지 소수검사(이전 단계문제를 참고함)
    flag = 0
    if i == 1:
        continue
    for x in range(2, i):
        if i%x == 0:
            flag = 1
            break
    if flag == 1:
        continue
    else:
        num_sosu.append(i) #소수인 경우 리스트에 추가
if len(num_sosu)>0: #소수가 있는 경우
    print(sum(num_sosu))
    print(min(num_sosu))
else: #소수가 없는 경우
    print(-1)
