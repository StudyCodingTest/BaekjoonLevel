#문제: 설탕 배달
#번호: 2839
#시간: 64ms

weight = int(input())
ans = 0
while weight>0: #무게가 0보다 클 때까지 반복
    if weight%5 == 0: #5의 배수가 되는지 지속적으로 검사한 후 된다면 즉시 5로 나눠줌
        ans += weight//5
        print(ans)
        break #break를 하지 않으면 weight가 0보다 작아서 else문이 실행됨
    weight -= 3 #3씩 지속적으로 감소
    ans += 1 #3씩 1번 감소할때마다 1씩 증가
    if weight == 0: #weight가 0이되면 즉, 단 한번도 5의 배수가 되지 않으면서 3으로 나눠떨어진 경우
        print(ans)
        break
else:
    print(-1) #한번도 5와 3의 배수가 되지않는 경우 -1출력
                #ans는 증가된 상태지만 출력하지 않으므로 상관없음

##while-else문은 while문의 조건이 만족하지않을 경우 else문을 실행
