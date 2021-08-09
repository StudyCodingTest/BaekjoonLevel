# 설탕 배달
# 72ms
N = int(input())
five_kg, r  = divmod(N, 5)
while r % 3 != 0 and five_kg >= 0:
    five_kg -= 1
    r += 5
print(five_kg+r//3 if five_kg >= 0 else -1)