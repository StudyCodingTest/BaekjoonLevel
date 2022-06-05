import sys
input = sys.stdin.readline

all_site, find_site = map(int,input().split())

passwords = dict()
for _ in range(all_site):
    site, pw = input().split()
    passwords[site] = pw


for _ in range(find_site):
    print(passwords[input().rstrip("\n")])