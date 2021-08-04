#문제: 벌집, 시간: 80ms
a = int(input())
path = 1
room = 6
last_room = 1

while a > last_room:
    path += 1
    last_room += room
    room += 6

print(path)
