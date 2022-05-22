import sys

# N = int(sys.stdin.readline())

# array = [0] * N
# dp_max = [0] * N
# dp_min = [0] * N
# for k in range(N):
#     array[k] = list(map(int, sys.stdin.readline().split()))
#     dp_max[k] = list([0] * 3)
#     dp_min[k] = list([0] * 3)

# dp_max[0] = array[0]
# dp_min[0] = array[0]

# for i in range(1,N):
#     for j in range(3):
#         if j == 0:
#             up_left_max = 0
#             up_left_min = 10
#         else:
#             up_left_max = dp_max[i-1][j-1]
#             up_left_min = dp_min[i-1][j-1]
#         if j == 2:
#             up_right_max = 0
#             up_right_min = 10
#         else:
#             up_right_max = dp_max[i-1][j+1]
#             up_right_min = dp_min[i-1][j+1]
#         up_max = dp_max[i-1][j]
#         up_min = dp_min[i-1][j]
#         dp_max[i][j] = array[i][j] + max(up_left_max, up_max, up_right_max)
#         dp_min[i][j] = array[i][j] + min(up_left_min, up_min, up_right_min)
        
    
# result_max = max(dp_max[N-1][0], dp_max[N-1][1], dp_max[N-1][2])
# result_min = min(dp_min[N-1][0], dp_min[N-1][1], dp_min[N-1][2])

# print(result_max, result_min)

N = int(sys.stdin.readline())

dp_max = [0] * 3
dp_min = [0] * 3
temp_max = [0] * 3
temp_min = [0] * 3

for i in range(N):
    a, b, c = map(int,sys.stdin.readline().split())
    for j in range(3):
        
        if j == 0:
            dp_max[0] = a + max(temp_max[0], temp_max[1])
            dp_min[0] = a + min(temp_min[0], temp_min[1])
        elif j == 1:
            dp_max[1] = b + max(temp_max[0], temp_max[1], temp_max[2])
            dp_min[1] = b + min(temp_min[0], temp_min[1], temp_min[2])
        else:
            dp_max[2] = c + max(temp_max[1], temp_max[2])
            dp_min[2] = c + min(temp_min[1], temp_min[2])
            
    for k in range(3):
        temp_max[k] = dp_max[k]
        temp_min[k] = dp_min[k]
        
print(max(temp_max[0], temp_max[1], temp_max[2]), min(temp_min[0], temp_min[1], temp_min[2]))