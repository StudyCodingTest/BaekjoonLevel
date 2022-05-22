import sys

n = int(sys.stdin.readline())

# n=3인 별 모델
star = [[0]*3]*3        
star[0] = [' ',' ','*',' ',' ']
star[1] = [' ','*',' ','*',' ']
star[2] = ['*','*','*','*','*']


height = 3
line = 5
#n = 3인 모델의 밑변과 높이

def func_reculsive(N, before, height, line):
    # before 별 모델 3개가 들어갈 배열
    after = [[" "] * (line*2+1) for _ in range(height*2)]
    
    for i in range(height):
        after[i][height:height+line] = before[i]     #첫번째 before 별 모델 복사
        after[i+height][:line] = before[i]           #두번째 before 별 모델 복사
        after[i+height][line+1:line*2+1] = before[i] #세번째 before 별 모델 복사
        #1번째 별 모델은 맨 위에서 시작하기 때문에 i=0 에서 시작
        #2번째 별 모델은 1번째 별 모델 밑에서 시작하기 때문에 height 만큼 더해준 위치에서 시작, 3번째도 마찬가지
        #line은 밑변인데 공백이 전 모델의 높이만큼 있기 때문에 height를 쓴것임. 예를 들어 n=6인 after 모델이면 그 전 모델은 n = 3인 모델이다. n = 3인 모델의 높이는 3, 밑변은 5이다.
        
    result = after
    #result를 다음 재귀에서 before로 쓰기위한 작업이자 재귀가 끝났을때 최종 결과값임.
    N = N // 2
    #무한재귀를 막기위한 장치. N이 3이되면 재귀는 끝이난다. 
    height = height * 2
    line = line * 2 + 1
    #현재 모델의 높이와 밑변으로 업데이트를 하는 것인데 다음 재귀에서 위의 for문에서 쓰는것처럼 이전 모델의 높이와 밑변을 사용하기 때문에 지금 업데이트 하는 것.
    
    if N == 3:
        return result
    #재귀 끝
    else:
        return func_reculsive(N, result, height, line)
    #N이 3이 될때까지 재귀

    
if n == 3:
    star_result = star
#n = 3인 모델은 맨위에 배열로 선언을 해놔서 그냥 프린트
else:
    star_result = func_reculsive(n, star, height, line)
#n = 3이 될때까지 재귀를 해서 복사해주면 원하는 모양이 나옴.
    
for j in star_result:
    print(''.join(j))