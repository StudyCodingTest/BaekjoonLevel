# The nearest two dot
# 2352ms
import sys
input = sys.stdin.readline

sorted_location = []
for _ in range(int(input())):
    x,y = list(map(int,input().split()))
    sorted_location.append((x,y))
sorted_location.sort() # sorting based on the x-coordinate

def get_dist(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def solution(l,r):
    if l==r: # cannot split
        return float("inf")
    else:
        m = (l+r)//2 
        # d1: left side min distance d2: right side min distance
        min_dist = min(solution(l,m), solution(m+1,r)) # find min(d1,d2)
        target_list = []
        # 1. find points with a distance less than d in the left and right regions
        
        # 1-1. based on the x-coordinate
        for i in range(m,l-1,-1):
            if (sorted_location[i][0] - sorted_location[m][0])**2 < min_dist:
                target_list.append(sorted_location[i])
            else: # because of sorting, after distance must be longer than min_dist
                break
        
        for j in range(m+1,r+1):
            if(sorted_location[j][0] - sorted_location[m][0])**2 < min_dist:
                target_list.append(sorted_location[j])
            else: # because of sorting, after distance must be longer than min_dist
                break
        # 1-2. based on the y-coordinate
        target_list.sort(key=lambda x:x[1])
        for i in range(len(target_list)-1):
            for j in range(i+1, len(target_list)):
                if(target_list[i][1] - target_list[j][1])**2 < min_dist:
                    dist = get_dist(target_list[i],target_list[j])
                    min_dist = min(min_dist,dist)
                else: # because of sorting, after distance must be longer than min_dist
                    break
        return min_dist

# overlap dot --> the nearest distance = 0
if len(sorted_location) != len(set(sorted_location)):
    print(0)
else:
    print(solution(0,len(sorted_location)-1))


