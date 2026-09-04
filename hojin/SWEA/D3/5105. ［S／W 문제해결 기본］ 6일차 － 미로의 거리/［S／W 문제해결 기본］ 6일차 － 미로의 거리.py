from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]
    start_r = 0
    start_c = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_r = i
                start_c = j
    # 0이 통로 1이 벽, 2가 출발, 3은 도착

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = deque([(start_r, start_c, 0)])
    visited = {(start_r, start_c)}
    while queue:

        row, col, dist = queue.popleft()

        if maze[row][col] == 3:
            result = dist-1
            break

        for i in range(4):
            nrow = row + dr[i]
            ncol = col + dc[i]

            if 0<=nrow<N and 0<=ncol<N and maze[nrow][ncol] != 1 and (nrow, ncol) not in visited:
                queue.append((nrow,ncol,dist+1))
                visited.add((nrow,ncol))

    print(f'#{test_case} {result}')
