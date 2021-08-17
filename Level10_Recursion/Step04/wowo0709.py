# 하노이 탑 이동 순서
# 920ms
def hanoi(fromV, byV, toV, n):
    global path
    if n == 1:
        path.append("{0} {1}".format(fromV, toV))
        return
    hanoi(fromV, toV, byV, n-1)
    path.append("{0} {1}".format(fromV, toV))
    hanoi(byV, fromV, toV, n-1)

path = []
hanoi(1, 2, 3, int(input()))
print(len(path))
print(*path, sep='\n')