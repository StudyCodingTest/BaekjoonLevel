# 카드2
# 264ms
from collections import deque
cards = deque(reversed([n for n in range(1,int(input())+1)]))
while len(cards) > 1:
    cards.pop()
    cards.rotate(1)

print(cards[0])