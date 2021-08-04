# 크로아티아 알파벳
# 72ms
cro_words = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = input()
answer = len(s)
for word in cro_words:
    answer += (1-len(word))*s.count(word)
    s = s.replace(word,'_')
print(answer)