# 다이얼
# 156ms
from string import ascii_uppercase
word_num_dict = dict(zip(ascii_uppercase, '2'*3+'3'*3+'4'*3+'5'*3+'6'*3+'7'*4+'8'*3+'9'*4))

print(sum([int(word_num_dict[word])+1 for word in input()]))