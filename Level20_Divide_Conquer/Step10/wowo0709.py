# 가장 가까운 두 점
# 2296ms
import sys
input = sys.stdin.readline

# 두 점 사이 거리 함수
def get_dist(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

# 분할 정복 함수
def solution(l,r):
    if l==r: # 한 점만 남은 경우
        return float("inf")
    else:
        m = (l+r)//2 
        # 경계선 기준 왼쪽 영역과 오른쪽 영역 중 최단 거리로 설정 (중앙의 점들 제외)
        min_dist = min(solution(l,m), solution(m+1,r))
        # 비교의 후보가 될 좌표들
        target_list = []

        ### 중앙의 점을 포함한 거리들 중 min_dist 미만의 거리가 있는지 탐색
        # x좌표 기준으로 내림차순 탐색 (중앙의 기준점과 다른 점 사이의 거리)
        for i in range(m,l-1,-1): # 왼쪽 영역: 오른쪽에서 왼쪽으로
            if (sorted_location[i][0] - sorted_location[m][0])**2 < min_dist:
                target_list.append(sorted_location[i])
            else: # x 좌표 기준으로 정렬되어 있기 때문에 탐색 중지
                break
        # x좌표 기준으로 오름차순 탐색 (중앙의 기준점과 다른 점 사이의 거리)
        for j in range(m+1,r+1): # 오른쪽 영역: 왼쪽에서 오른쪽으로
            if(sorted_location[j][0] - sorted_location[m][0])**2 < min_dist:
                target_list.append(sorted_location[j])
            else: # x 좌표 기준으로 정렬되어 있기 때문에 탐색 중지
                break

        # y좌표 기준으로 오름차순 탐색 (임의의 두 점 사이의 거리)
        target_list.sort(key=lambda x:x[1])
        for i in range(len(target_list)-1):
            for j in range(i+1, len(target_list)):
                if(target_list[i][1] - target_list[j][1])**2 < min_dist:
                    dist = get_dist(target_list[i],target_list[j])
                    min_dist = min(min_dist,dist)
                else: # y 좌표 기준으로 정렬되어 있기 때문에 해당 기준 y좌표에 대한 탐색 중지
                    break
        return min_dist


n = int(input())
sorted_location = [tuple(int(c) for c in input().split()) for _ in range(n)]
sorted_location.sort() # x 좌표 기준 정렬

if len(sorted_location) != len(set(sorted_location)): # 동일한 점이 있을 경우
    print(0)
else:
    print(solution(0,len(sorted_location)-1))