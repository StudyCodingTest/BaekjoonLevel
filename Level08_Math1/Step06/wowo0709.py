# 부녀회장이 될테야
# 92ms
people = [[i for i in range(15)] for _ in range(15)]
for _ in range(int(input())):
    k, n = int(input()), int(input())
    for i in range(1, k+1):
        for j in range(1, n+1):
            if people[i][j] == j: # 초기화 전
                people[i][j] = people[i][j-1] + people[i-1][j]
    print(people[k][n])