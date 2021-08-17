#문제: 분해합
#번호: 2231
#시간: 2864ms


def divide_sum(m): # 분해합을 수행하는 함수
    m_str = str(m) # 입력받은 수를 문자열 형태로 변환
    m_list = [m_str[i] for i in range(len(m_str))] # 각 자리수로 분해
    n_list = [int(m_list[x]) for x in range(len(m_list))]# 각 자리수를 정수형으로 변환
    n = m + sum(n_list) # 분해합
    return n


m = int(input())
nums = [i for i in range(1, m+1)] # 1부터 입력받은 수 m까지 리스트를 만듦
ans = [] # 정답을 저장할 리스트
for x in range(m): # 생성자가 분해합보다 클 수는 없으므로 m까지만 검사
    if m == divide_sum(nums[x]): # 분해합과 m이 일치한다면 ans리스트에 추가
        ans.append(x+1)
if len(ans) == 0: #생성자가 없으면 '0'출력
    print(0)
else: # 생성자가 있다면 그 중 가장 작은 수를 출력
    print(ans[0])
