# 소트인사이드
# 76ms

import sys

num = input()

lst = list(num)
lst.sort(reverse=True)
print("".join(lst))
