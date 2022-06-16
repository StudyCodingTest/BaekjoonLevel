import sys
input = sys.stdin.readline
N = int(input())

from copy import deepcopy
values = list(map(int, input().rstrip().split()))
prev_scores = [[num,num] for num in values] # max, min
cur_scores = [[num,num] for num in values] # max, min
for i in range(1,N):
    values = list(map(int, input().rstrip().split()))
    cur_scores[0] = [values[0]+max([mx for mx,mn in prev_scores[:2]]), values[0]+min([mn for mx,mn in prev_scores[:2]])]
    cur_scores[1] = [values[1]+max([mx for mx,mn in prev_scores]), values[1]+min([mn for mx,mn in prev_scores])]
    cur_scores[2] = [values[2]+max([mx for mx,mn in prev_scores[1:]]), values[2]+min([mn for mx,mn in prev_scores[1:]])]
    prev_scores = deepcopy(cur_scores)
print(max([mx for mx,mn in cur_scores]), min([mn for mx,mn in cur_scores]))