# 문제 : OX 퀴즈 , 문제 번호 : 8958, 소요 시간 : 84ms
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다.
# O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지
# 연속된 O의 개수가 된다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고,
# 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
# 문자열은 O와 X만으로 이루어져 있다.

# 출력
# 각 테스트 케이스마다 점수를 출력한다.

num_testcase = int(input()) # 테스트 케이스 개수


for i in range(num_testcase) : # 0~ (테스트 개수 - 1) 만큼
    score_sum = 0 # 총 점수 초기화
    add_score = 0 # 누적 점수 초기화
    quiz_result = input()  # ox 퀴즈 결과를 입력 받음
    for i in range(len(quiz_result)) : # 입력 받은 ox 퀴즈 결과의 개수 만큼 돈다. 
        if quiz_result[i] == 'O' :   # 그 때 퀴즈 결과가 O이면
            add_score += 1  # 누적 점수 1 증가 시킨다.
            score_sum += add_score  # 현재 점수에 누적 점수만큼을 더한 게 총점이다.
        elif quiz_result[i] == 'X' : # 퀴즈 결과가 X이면
            add_score = 0  # 누적 점수를 0으로 돌린다.
    print(score_sum) # 총 점수 출력
    

