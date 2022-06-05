import sys
input = sys.stdin.readline

# 초기 조건
n = int(input())
length = int(input())
string = input()

slice_count = 0 # IOI의 개수
pn_count = 0 # Pn의 개수

for i in range(length-2):
    if string[i] == "O":
        continue
    else:
        if string[i+1] == "O" and string[i+2] == "I":
            slice_count += 1

            if slice_count == n:
                pn_count += 1
                slice_count -= 1
        else:
            slice_count = 0

print(pn_count)