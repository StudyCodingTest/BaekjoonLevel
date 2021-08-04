# 알파벳 찾기
# 140ms
from string import ascii_lowercase
S = input()
print(*[S.find(alpha) for alpha in ascii_lowercase])