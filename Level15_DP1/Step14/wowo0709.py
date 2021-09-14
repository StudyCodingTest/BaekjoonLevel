# LCS
# 724ms
s1, s2 = input(), input()
lcs = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
for i in range(1,len(s2)+1):
    for j in range(1,len(s1)+1):
        if s1[j-1] == s2[i-1]: lcs[i][j] = lcs[i-1][j-1] + 1
        else: lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
print(lcs[-1][-1])