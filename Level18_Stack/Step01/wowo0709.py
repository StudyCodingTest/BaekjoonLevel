# 스택

# 76ms
import sys
input = sys.stdin.readline

n = int(input())
command = []
top = -1
stack = []
for i in range(n):
    command = input().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
        top += 1
    elif command[0] == 'pop':
        if top != -1:
            top -= 1
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(int(top==-1))
    elif command[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])


# 76ms
import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.top_idx = -1
        self.stack = []
    def push(self,x):
        self.stack.append(x)
        self.top_idx += 1
    def pop(self):
        if self.top_idx != -1:
            self.top_idx -= 1
            return self.stack.pop()
        return -1
    def size(self):
        return len(self.stack)
    def empty(self):
        return int(self.top_idx==-1)
    def top(self):
        if self.top_idx == -1:
            return -1
        return self.stack[self.top_idx]

n = int(input())
command = []
s = Stack()
for i in range(n):
    command = input().split()
    if command[0] == 'push':
        s.push(int(command[1]))
    elif command[0] == 'pop':
        print(s.pop())
    elif command[0] == 'size':
        print(s.size())
    elif command[0] == 'empty':
        print(s.empty())
    elif command[0] == 'top':
        print(s.top())