# 최대 공약수와 최소 공배수
# 72ms
from math import gcd
a,b = map(int, input().split())
print(gcd(a,b),a*b//gcd(a,b),sep='\n')

'''
def gcd(a, b):
	while b:
		a, b = b, a%b
	return a
'''