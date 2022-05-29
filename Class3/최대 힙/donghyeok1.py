import sys
import heapq

N = int(sys.stdin.readline())

h = []
result = []
for i in range(N):
    x = int(sys.stdin.readline())
    heapq.heappush(h, -x)
    #heapq 라이브러리의 heappush 함수는 파라미터를 두개 가짐
    #첫 번째 파라미터는 append 할 list
    #두 번째 파라미터는 append 할 value이다.
    #이렇게 하나씩 넣게 되면 
    #![캡처](https://user-images.githubusercontent.com/95459089/170843465-4142b916-d3eb-4f95-a0b9-2279f1bc76c5.PNG)
    #위 그림 처럼 트리를 형성하게 됨.
    #이렇게 형성되어 있는 트리에 어떠한 수를 삽입하게 된다면
    #![캡처](https://user-images.githubusercontent.com/95459089/170843521-82b22d87-a8f8-4d71-8fa8-b2e5fd8a5b9e.PNG)
    #위 그림처럼 맨 밑에서부터 부모 노드랑 비교를 해가면서 올라가게 된다. 
    #파이썬의 heapq는 최소힙이 default이고 최대힙으로 주려면 위 코딩처럼 value값에
    #-를 붙여서 넣어주고 pop 할때도 -를 붙여서 빼야한다.
    #그래서 0이 나오기 전까지 heappush를 하면서 트리를 형성해주고
    #0이 나오면 맨 위에 있는 수를 빼준다. 그것이 max이기 때문에.
    #![캡처](https://user-images.githubusercontent.com/95459089/170843608-6f05e17d-c9f1-41de-a9b6-12512d79a24a.PNG)
    #heappop을 해서 맨 위에 수를 제거해주면 가장 마지막 노드가 루트 노드의 위치에 오게한다.
    #![캡처](https://user-images.githubusercontent.com/95459089/170843650-18bbbab2-cfe9-4a4e-8796-dff5d461705f.PNG)
    #위 그림처럼 루트 노드로 보내고 바로 아래 자식 노드 두 개와 비교해서 위치 시킨다.
    
    if x == 0:
        result.append(-heapq.heappop(h))
    #0이 나오기 전까지 계속 push를 해서 트리 형성
    #0이 나오면 루트 노드 pop
    #그러면 다시 heapify()를 통해 트리 형성
    #만약 트리가 비어있다면 0을 pop해줌.
        
for i in range(len(result)):
    print(result[i])
        
    