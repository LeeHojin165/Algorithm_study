import heapq

T = int(input())

for test_case in range(1, T + 1):
    result = 0

    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    queue = []
    distance = [[float('inf')] * N for _ in range(N)]


    start_r = 0
    start_c = 0
    distance[start_r][start_c] = 0
    heapq.heappush(queue, (distance[start_r][start_c], start_r, start_c))

    min_time = float('inf')
    while heapq:
        time,r, c = heapq.heappop(queue)

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        if r == N-1 and c == N-1:
            min_time = time
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if time + matrix[nr][nc] < distance[nr][nc]:
                    distance[nr][nc] = time + matrix[nr][nc]
                    heapq.heappush(queue, (distance[nr][nc], nr, nc))

    result = min_time
    print(f'#{test_case} {result}')
