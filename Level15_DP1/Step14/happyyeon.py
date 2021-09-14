# LCS
# 700ms

string1 = input()
string2 = input()
dp=[[0]*1001 for _ in range(1001)] # dp는 (1,1)부터 시작
len_str1 = len(string1) #6
len_str2 = len(string2) #6
# string1 : A -> A ->   A   -> ... -> AC -> AC -> ...
# string2 : C -> CA -> CAP -> ... ->   C  -> CA -> ...
for i in range(len_str1) :# 0~5
    for j in range(len_str2) : # 0~5
        # [AC,CAPC]LCS = [A,CAP]LCS + 1
        if string1[i] == string2[j]:
            dp[i+1][j+1] = dp[i][j]+1 # dp[1][1] = 1
        # [ACAYKP,CAPCAK]LCS = max([ACAYKP,CAPCA]LCS, [ACAYK,CAPCAK]LCS)
        else :
            dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1]) #dp[1][1] = 0

print(dp[len_str1][len_str2])



# lst1 = [[0]*3]*3
# lst2 = [[0]*3 for _ in range(3)]
# print(lst1)
# print(lst2)