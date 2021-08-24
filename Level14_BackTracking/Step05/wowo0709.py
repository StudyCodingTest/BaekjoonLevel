# N-Queen
# 14396ms(PyPy3)
col_loc = [] # 0~7번째 행에 위치한 열의 위치
def find_nqueen(N, row, cnt):
    global col_loc
    if row == N:
        return cnt+1

    for col in range(N):
        for line in range(len(col_loc)):
            if col == col_loc[line] or row + col == line + col_loc[line]\
                                    or row - col == line - col_loc[line]:
                break
        else:
            col_loc.append(col)
            cnt = find_nqueen(N,row+1,cnt)
            col_loc.pop()

    return cnt

print(find_nqueen(int(input()),0,0))


# 6860ms(PyPy3)
n = int(input())
count = 0
column,rightup,rightdown = [False]*n,[False]*(2*n-1),[False]*(2*n-1)

def NQueen(line):
  global count
  if line == n:
    count += 1
    return
  else:
    for index in range(n):
      if not (column[index] or rightup[line+index] or rightdown[line-index+n-1]):
        column[index] = rightup[line+index] = rightdown[line-index+n-1] = True
        NQueen(line+1)
        column[index] = rightup[line+index] = rightdown[line-index+n-1] = False

NQueen(0)
print(count)