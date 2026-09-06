import heapq

T = int(input())

for test_case in range(1, T + 1):
    result = float('inf')
    # 출발 0,0 도착 n-1,n-1

    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    q = []
    heapq.heappush(q, (matrix[0][0], 0, 0))
    distance = [[float('inf')] * n for _ in range(n)]
    distance[0][0] = matrix[0][0]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while q:
        sum_val, row, col = heapq.heappop(q)

        if row == n - 1 and col == n - 1:
            result = sum_val

        for i in range(4):
            nrow = row + dr[i]
            ncol = col + dc[i]

            if 0 <= nrow < n and 0 <= ncol < n:
                if matrix[nrow][ncol] + sum_val < distance[nrow][ncol]:
                    heapq.heappush(q, (sum_val + matrix[nrow][ncol], nrow, ncol))
                    distance[nrow][ncol] = matrix[nrow][ncol] + sum_val

    print(f'#{test_case} {result}')
