#문제: 그룹 단어 체커, 시간: 84ms
import sys


word_num = int(sys.stdin.readline())
word = []
group_word = 0
flag = 0
for _ in range(word_num):
    word.append(input())
print(word)

for i in range(len(word)):
    find_group = []
    for alpha in range(len(word[i])):
        if word[i][alpha] in find_group and word[i][alpha] != word[i][alpha-1]:
            flag = 1
            break
        find_group.append(word[i][alpha])
        #print(find_group)
        #print(flag)
    if flag == 1:
        flag = 0
        continue
    group_word += 1
    #print(find_group)
print(group_word)
