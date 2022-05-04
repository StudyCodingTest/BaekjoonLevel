# import sys
# input = sys.stdin.readline

# m = int(input())
# s = set()
# for _ in range(m):
#     temp = input().strip().split()
#     # [only command]
#     if len(temp) == 1:
#         command = temp[0]
#         if command == "all":
#             s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
#         if command == "empty":
#             s = set()
#     # [command,x]
#     else:
#         command,x = temp[0],temp[1]
#         x = int(x)

#         if command == "add":
#             s.add(x)
#         if command == "remove" and x in s:
#             s.remove(x)
#         if command == "check":
#             if x in s:
#                 print(1)
#             else:
#                 print(0)
#         if command == "toggle":
#             if x in s:
#                 s.remove(x)
#             else:
#                 s.add(x)

import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    # [command,x]
    try:
        command,x = input().split()
        x = int(x)

        if command == "add":
            s.add(x)
        if command == "remove" and x in s:
            s.remove(x)
        if command == "check":
            if x in s:
                print(1)
            else:
                print(0)
        if command == "toggle":
            if x in s:
                s.remove(x)
            else:
                s.add(x)
    # [only command]
    except:
        command = input()
        
        if command == "all":
            s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        if command == "empty":
            s = set()