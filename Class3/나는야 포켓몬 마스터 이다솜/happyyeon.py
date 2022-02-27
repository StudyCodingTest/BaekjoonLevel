# -*-coding:utf-8-*-
# ���¾� ���ϸ� ������ �̴ټ�

# �ð� �ʰ� �ڵ� �ð� ���⵵�� O(N)
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
# pocketmons = [0]*(n+1)
# for i in range(1,n+1):
#     pocketmons[i] = input().strip()

# for i in range(m):
#     num_or_pocketmon = input().strip()
#     try:
#         print(pocketmons[int(num_or_pocketmon)])
#     except ValueError:
#         print(pocketmons.index(num_or_pocketmon))

# ���� Dictonary�� ����ؾ��� �ð����⵵�� O(1)�̱� ������

dict = {}

for num in range(1,n+1):
    pocketmon = input().rstrip()
    dict[num] = pocketmon
    dict[pocketmon] = num

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])





