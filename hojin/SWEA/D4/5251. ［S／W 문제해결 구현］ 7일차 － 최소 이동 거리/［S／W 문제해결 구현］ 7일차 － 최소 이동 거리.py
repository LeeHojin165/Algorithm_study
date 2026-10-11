import heapq
from collections import defaultdict
T = int(input())

for tc in range(1,T+1):
    #n번 지점과 e개의 도로
    n, e = map(int, input().split())

    graph = defaultdict(list)

    for i in range(e):
        #시작, 끝, 가중치
        s, e, w = map(int, input().split())
        #단방향
        graph[s].append((e,w))

    q = []
    distance = [float('inf')] * (n+1)
    heapq.heappush(q,(0,0))
    while q:
        node, dist = heapq.heappop(q)

        for end, weight in graph[node]:
            if  dist + weight < distance[end]:
                distance[end] = dist + weight
                heapq.heappush(q,(end, dist + weight))

    answer = distance[n]
    print(f'#{tc} {answer}')