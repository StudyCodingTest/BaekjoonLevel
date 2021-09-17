# 회의실 배정
# 5156ms
N = int(input())
# starting time, ending time
# 1, 3 / 4, 4 / 3, 4 -> sorting
meetings = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda m:(m[1],m[0]))
end_time = meetings[0][1]
cnt = 1
for i in range(1,len(meetings)):
    if end_time <= meetings[i][0]:
        end_time = meetings[i][1]
        cnt += 1
print(cnt)

