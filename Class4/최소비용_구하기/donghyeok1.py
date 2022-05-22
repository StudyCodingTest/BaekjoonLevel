import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

table = [[0] * 3 for _ in range(M)]

for i in range(M):
    table[i] = list(map(int, sys.stdin.readline().split()))
route = [0] * 2

route[0], route[1] = map(int, sys.stdin.readline().split())
min_list = []
sum = 0
def recursive(table, route, arrive, M, min_list, sum):
    prev_sum = 0
    for i in range(M):
        if table[i][1] == arrive:
            sum += table[i][2]
            if table[i][0] != route[0]:
                arrive_1 = table[i][0]
                recursive(table, route, arrive_1, M, min_list, sum)
                sum -= table[i][2]
            else:
                min_list.append(sum)
                sum -= table[i][2]
                i = M
                
                
                    
                    
recursive(table, route, route[1], M, min_list, sum)
min = min_list[0]
for j in range(1,len(min_list)):
    if min > min_list[j]:
        min = min_list[j]
        
print(min)