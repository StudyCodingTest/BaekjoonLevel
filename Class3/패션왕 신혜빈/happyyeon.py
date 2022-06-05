import sys
input = sys.stdin.readline

# 옷 정보 Dictionary
for _ in range(int(input())):
    clothes_dict = dict()
    for _ in range(int(input())):
        clothes, category = input().split()
        
        if category in clothes_dict.keys():
            clothes_dict[category].append(clothes)
        else:
            clothes_dict[category] = [clothes]

    answer = 1

    for category in clothes_dict.keys():
        answer *= len(clothes_dict[category])+1

    print(answer-1)

