#문제: 분수찾기, 시간: 84ms
a = int(input())
b = a
count = 0
line = 1

while a>0:
    count += 1
    a -= line
    line += 1

line = 0
for i in range(1, count+1):
    line += i

print(count, line)

mom = 1
son = 1
if count%2 == 0:
    son = count
    line_move = line - b

    mom += line_move
    son -= line_move
    print(f"{son}/{mom}")

else:
    mom = count
    line_move = line - b

    son += line_move
    mom -= line_move
    print(f"{son}/{mom}")

