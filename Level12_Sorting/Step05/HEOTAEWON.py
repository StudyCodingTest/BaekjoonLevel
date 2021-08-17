#문제: 소트인사이드
#번호: 1472
#시간: 76ms


n = int(input())
n_str = str(n) # 입력받은 수를 문자열로 변환
ans = [] # 각 자리수를 저장할 리스트 생성
for i in range(len(n_str)): # 각 자리수를 리스트에 추가
    ans.append(n_str[i])
ans.sort(reverse= True) # 내림차순으로 정렬
for x in range(len(ans)): #하나씩 이어서 출력
    print(ans[x], end='')
