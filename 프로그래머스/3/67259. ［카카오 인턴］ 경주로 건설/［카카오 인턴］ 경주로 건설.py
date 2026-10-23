import heapq


def solution(matrix):
    answer = 0

    # 기본적으로 다익스트라를 쓰며, 다음 칸으로 갈때 방향이 달라지면 500을 아니면 100을 넣어서 최소비용을 return한다.

    # 출발 0,0 도착 n-1,n-1

    n = len(matrix[0])
    q = []
    # 시작은 하 아니면 우

    # 비용, 좌표, 방향
    heapq.heappush(q, (0, 0, 0, 0))

    #해당 좌표에서 방향이 (0,1,2,3)중 하나일때 거리를 넣는다. 즉 4개의 상태를 3차원 배열에 넣는 것

    #원래는 거리 dist만 넣지만, 지금은 [(거리, 방향)]을 4개 이하로 넣기 때문에 배열
    #근데 그러면 초기화를 어떻게 할까 >
    distance = [[[float('inf') for _ in range(4)]  for _ in range(n)] for _ in range(n)]

    for i in range(4):
        distance[0][0][i] = 0
    


    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        cost, r, c, cur_dir = heapq.heappop(q)
        # print(cost, r, c, cur_dir)

        if distance[r][c][cur_dir] < cost:
            continue

        if r == n - 1 and c == n - 1:
            answer = min(answer,cost)

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 0:
                # 직진하면 가중치
                w = 100
                # dir이 cur_dir과 다르면 w에 500 추가
                if cost != 0 and dir != cur_dir:
                    w += 500

                if cost + w < distance[nr][nc][dir]:
                    # distance 갱신하고
                    distance[nr][nc][dir] = cost + w
                    # 힙에 넣는다.
                    heapq.heappush(q, (cost + w, nr, nc, dir))

    #print(distance[n - 1][n - 1])
    answer = min(distance[n - 1][n - 1])
    
    return answer

