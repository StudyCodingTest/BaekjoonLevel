# 단어 공부
# 152ms
from collections import Counter

s = input().upper()
try: 
    first, second = Counter(s).most_common(2)
    print(first[0] if first[1] > second[1] else '?')
except: # 길이가 1인 경우
    print(s)