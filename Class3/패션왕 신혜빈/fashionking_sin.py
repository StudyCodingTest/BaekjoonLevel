import sys
sys.stdin = open('input', 'r')

T =int(input())

for _ in range(T):
    n = int(input())
    fasion = {}
    ans = 1 # 값을 계속 곱해줄 것이기 때문에 처음에 1로 해준다.
    for _ in range(n):
        cloth, genre = input().split()

        if genre in fasion: # 해당 종류의 의상이 이미 있는지 검사
            fasion[genre][1] += 1 # 이미 있다면, 해당 종류의 의상 개수 + 1
        else: # 만약 없다면, 새로운 종류의 의상으로 추가해준다.
            fasion[genre] = [cloth, 2] # 의상을 선택하지 않는 경우도 있기 때문에 개수를 2로 해준다.

    for i in fasion: # fashion dictionary로부터 key 값을 받아온다.
        #print(i, fasion[i][1])
        ans *= fasion[i][1] # 의상 종류별 개수만큼 ans에 곱해준다.

    print(ans - 1) # 모두 선택하지 않는 경우는 빼야하므로 -1 하여 출력한다. 
