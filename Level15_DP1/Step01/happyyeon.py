# 피보나치 함수
# 76ms
import sys
input = sys.stdin.readline
# 테스트 케이스
for _ in range(int(input())) :
    def fibonacci(num) :
        if num == 0 :
            return 0
        elif num == 1 :
            return 1
        else :
            fib_nums = [0,1] # 피보나치 수 배열
            
            for i in range(2,num+1) :
                fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
            
            return fib_nums[num]
    num = int(input())
    print(fibonacci(num-1), fibonacci(num))
