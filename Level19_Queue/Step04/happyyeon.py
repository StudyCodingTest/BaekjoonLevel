#-*- coding: utf-8 -*-
# ������ ť
# 80ms

# �߿䵵 ť�� �̵��� �ε��� ť�� �̵��� ���ÿ� �ݿ��ϴ� ���� ����Ʈ�̴�.
import sys
input = sys.stdin.readline

for _ in range(int(input())) : # �׽�Ʈ ���̽�
    n,m = map(int,input().split())
    importants = list(map(int,input().split())) # �߿䵵 ť
    list_index = list(range(len(importants))) # �� �߿䵵�� �ε�����
    list_index[m] = "target" # m��° ��ġ�� �ε��� = Ÿ��

    order = 0 # ��� ����

    while True :
        if importants[0] == max(importants) : #ù��° ���Ұ� �ִ��̶�� ��¼��� 1 ����
            order += 1

            if list_index[0] == "target" : #���ÿ� �� ���Ұ� Ÿ���̶�� �ش� ������ ���
                print(order)
                break
            else : # target�� �ƴ϶��
                importants.pop(0) # �׳� ������
                list_index.pop(0) # �ε����� �׳� ������
        else : # ù ��° ���Ұ� �ִ��� �ƴ϶��
            # ���Ҹ� ť ���� ������
            importants.append(importants.pop(0))
            # �� �ε����� ����Ʈ ���� ������
            list_index.append(list_index.pop(0))

