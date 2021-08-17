# 블랙잭
# 152ms

import sys

num_field_card, black_jack = map(int,sys.stdin.readline().split()) # N, M

field_cards = list(map(int,sys.stdin.readline().split())) # 주어진 카드 리스트
card_sum = 0 # 카드 총합

# 세 개의 카드
for first_card in field_cards :
    for second_card in field_cards[field_cards.index(first_card)+1:] :
        for third_card in field_cards[field_cards.index(second_card)+1:] :
            if first_card + second_card + third_card > black_jack : 
                continue
            else :
                card_sum = max(card_sum, first_card + second_card + third_card)

print(card_sum)