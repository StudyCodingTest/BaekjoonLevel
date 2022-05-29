import queue
import sys
from collections import deque

# def reverse(queue):
#     list_len = len(queue)
#     for i in range(list_len // 2):
#         tmp = queue[list_len - 1 - i]
#         queue[list_len-1-i] = queue[i]
#         queue[i] = tmp


def print_list(result):
    
    while True:
        if result == "error":
            print("error",end="")
            break
        print("[",end="")
        for i in range(len(result)-1):
            print(str(result[i]) + ",",end="")
        print(str(result[len(result)-1]) + "]",end="")
        break

T = int(sys.stdin.readline())

result = [[] for _ in range(T)]
input_string = [[] for _ in range(T)]
for i in range(T):
    queue = deque()
    
    input_string[i] = list(sys.stdin.readline())
    
    len_list = int(sys.stdin.readline())
    list_a = sys.stdin.readline()
    list_a = (list_a.replace("[", "").replace(","," ").replace("]","")).split()
    for k in range(len(list_a)):
        queue.append(list_a[k])
    
    if len_list != len(list_a):
        result[i] = "error"
        continue    
    for func in input_string[i]:
        if func == "R":
            queue.reverse()
        elif func == "D":
            a = len(queue)
            if len(queue) == 0:
                result[i] = "error"    
                break
            queue.popleft()
    if result[i] != "error":
        result[i] = queue
    
for j in range(T):
    print_list(result[j])
    print()

