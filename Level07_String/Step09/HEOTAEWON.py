#문제: 크로아티아 알파벳, 시간: 76ms
import sys


changed = sys.stdin.readline()
count = 0

for i in range(len(changed)):
    if changed[i] == 'z' and changed[i+1] == '=':
        if changed[i-1] == 'd':
            continue
        else:
            count += 1
        continue
    elif changed[i] == '=':
        continue
    elif changed[i] == '-':
        continue
    elif changed[i] == 'j' and changed[i-1] == 'l':
        continue
    elif changed[i] == 'j' and changed[i-1] == 'n':
        continue
    elif changed[i] == '\n':
        continue
    else:
        count += 1
print(count)
