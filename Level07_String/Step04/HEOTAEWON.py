#문제: 문자열 반복, 시간: 76ms
import sys


test_times = int(sys.stdin.readline())

for _ in range(test_times):
    repeated_times, alpha = sys.stdin.readline().split()
    repeated_times = int(repeated_times)
    for n in alpha:
        print(n*repeated_times, end='')
    print('')
