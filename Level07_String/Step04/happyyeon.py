# 문제 이름 : 문자열 반복
# 문제 번호 : 2675
# 소요 시간 : 80ms

import sys

test_case = int(sys.stdin.readline()) # 테스트 케이스 입력 받음.  

for i in range(test_case) : # 테스트 케이스 개수 만큼 반복
    recursion_number , string = map(str, input().split()) # 반복 횟수와 문자열 입력 받음.
    int_recursion_number = int(recursion_number) # 아래 for문에서 int를 씌워주면 O(n)이고 따로 빼면 O(1)이라 생각해서 뺐는데 맞는지 모르겠음.
    for i in range(len(string)) :  # 문자열 길이만큼
        print(string[i] * int_recursion_number, end="") #공백 없이 반복 횟수 만큼 해당 문자를 출력

    print() 