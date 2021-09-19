# 잃어버린 괄호
# 136ms
import re
s = input()
s = re.split('([^0-9])', s)
for i in range(len(s)):
    if s[i].isdigit(): s[i] = str(int(s[i]))
    if s[i] == '-': s[i] = ')-('
print(eval('(' + ''.join(s) + ')'))

# ================================================
# 72ms
s = input().split('-')
for i in range(len(s)):
    s[i] = str(sum(list(map(int,s[i].split('+')))))
print(eval('-'.join(s)))

# ================================================
# 76ms
print(eval('-'.join([str(sum(list(map(int,eq.split('+'))))) for eq in input().split('-')])))