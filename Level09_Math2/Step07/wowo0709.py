# 직사각형에서 탈출
# 80ms
x, y, w, h = map(int, input().split())
print(min(x, w-x, y, h-y))