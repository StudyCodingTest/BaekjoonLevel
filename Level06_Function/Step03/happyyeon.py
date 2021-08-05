# 문제 : 한수 , 시간 : 68ms
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면
# 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을
# 말한다. N이 주어졌을 때, 1보다 크거나 같고
# N보다 작거나 같은 한수의 개수를 출력하는 프로그램

# 입력 
# 첫째 줄에 1000보다 작거나 같은 자연수 N이 주어진다.

# 출력 
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은
# 한수의 개수를 출력한다.

n = int(input()) # 자연수 N 입력 받음.
if 100 <= n <= 1000 :
    count_hansu = 0 # 한수 개수 초기화
    if n == 1000 : # 1000은 한수가 아님.
        n = 999
    for number in range(100, n+1) : # 100~ N
        temp, number_one_number = divmod(number, 10) # N의 1의 자리 수 저장
        number_hundred_number, number_ten_number = divmod(temp, 10) # N의 100, 10의 자리 수 저장

        if (number_hundred_number - number_ten_number) == (number_ten_number - number_one_number) :
            count_hansu += 1 # 등차수열 검사
    
    print(count_hansu + 99) # 1~99까지는 등차수열이기 때문.

elif (n < 100) :  # 100 미만의 수는 전부 한수
    print(n) 