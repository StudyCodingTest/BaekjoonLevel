import sys
input = sys.stdin.readline
# len(cmd)에 따라 분기 & set 사용
s = set()
for _ in range(int(input().rstrip())):
    cmd = input().rstrip().split()
    if len(cmd) == 1:
        cmd = cmd[0]
        if cmd == 'all':
            s = set([i for i in range(1,21)])
        elif cmd == 'empty':
            s.clear()
    else:
        cmd, x = cmd[0], int(cmd[1])
        if cmd == 'add':
            s.add(x)
        elif cmd == 'remove':
            s.discard(x)
        elif cmd == 'check':
            if x in s: print(1)
            else: print(0)
        elif cmd == 'toggle':
            if x in s: s.remove(x)
            else: s.add(x)



### 시간초과 ============================================================
'''
- 1번 풀이(초기 풀이, set사용)
import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input().rstrip())):
    cmd = input().rstrip()
    if cmd.startswith('add'):
        x = int(cmd.split()[-1])
        if x not in s:
            s.add(x)
    elif cmd.startswith('remove'):
        x = int(cmd.split()[-1])
        if x in s:
            s.remove(x)
    elif cmd.startswith('check'):
        x = int(cmd.split()[-1])
        if x in s: print(1)
        else: print(0)
    elif cmd.startswith('toggle'):
        x = int(cmd.split()[-1])
        if x in s: s.remove(x)
        else: s.add(x)
    elif cmd.startswith('all'):
        s = set([i for i in range(1,21)])
    elif cmd.startswith('empty'):
        s.clear()

- 2번 풀이(초기 풀이, dict 사용)
import sys
input = sys.stdin.readline

# by dict
dic = dict(zip([i for i in range(1,21)],[0]*20)) # key: 1~20, value: 0 or 1
for _ in range(int(input().rstrip())):
    cmd = input().rstrip()
    if cmd.startswith('add'):
        x = int(cmd.split()[-1])
        if dic[x] == 0:
            dic[x] += 1
    elif cmd.startswith('remove'):
        x = int(cmd.split()[-1])
        if dic[x] > 0:
            dic[x] -= 1
    elif cmd.startswith('check'):
        x = int(cmd.split()[-1])
        if dic[x] > 0: print(1)
        else: print(0)
    elif cmd.startswith('toggle'):
        x = int(cmd.split()[-1])
        if dic[x] > 0: dic[x] -= 1
        else: dic[x] += 1
    elif cmd.startswith('all'):
        for i in range(1,21): dic[i] = 1
    elif cmd.startswith('empty'):
        for i in range(1,21): dic[i] = 0


- 3번 풀이(정답 풀이에서 set만 dict로 교체했는데 시간초과...)
import sys
input = sys.stdin.readline

dic = dict(zip([i for i in range(1,21)],[0]*20)) # key: 1~20, value: 0 or 1
for _ in range(int(input().rstrip())):
    cmd = input().rstrip().split()
    if len(cmd) == 1:
        cmd = cmd[0]
        if cmd == 'all':
            dic = dict(zip([i for i in range(1,21)],[1]*20))
        elif cmd == 'empty':
            dic = dict(zip([i for i in range(1,21)],[0]*20))
    else:
        cmd, x = cmd[0], int(cmd[1])
        if cmd == 'add':
            dic[x] += 1
        elif cmd == 'remove':
            dic[x] -= 1
        elif cmd == 'check':
            if dic[x]: print(1)
            else: print(0)
        elif cmd == 'toggle':
            if dic[x]: dic[x] -= 1
            else: dic[x] += 1

'''