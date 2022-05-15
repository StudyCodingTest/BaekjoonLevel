import sys
import fractions
S = 1000000007
#b^(S-2) % S
def Recursive_Power(C,n):
    if n == 1:
        return C % S
    #recursive 탈출 조건
    if n % 2 == 0:
        y = Recursive_Power(C, n//2)
        return (y * y) % S
    
    else:
        y = Recursive_Power(C, (n-1) // 2)
        return (C * y * y) % S

m = int(sys.stdin.readline())

result_test = 0

# import fractions

# a = fractions.Fraction(1,2) #1/2
# b = fractions.Fraction(2,3) #2/3

# c = a+b #(1/2) + (2/3) = 7/6

# c.numerator #분자 = 7
# c.denominator #분모 = 6

for i in range(m):
    b, a = map(int, sys.stdin.readline().split())
    result_test += (fractions.Fraction(a, b))
    
C = result_test.denominator
n = result_test.numerator

result = ((n % S) * Recursive_Power(C, S-2)) % S

print(result)

    