# 문제 이름 : 택시 기하학
# 문제 번호 : 3053
# 소요 시간 : 76ms

import sys, math

radius = int(sys.stdin.readline())

print("{:.6f}".format(math.pi * (radius**2))) # 유클리드 기하학 : 파이 * r^2 = 원의 넓이
print("{:.6f}".format((radius**2) * 2)) # 비유클리드 기하학 : r^2 / 2 * 4 = r^2 * 2 = 원의 넓이
