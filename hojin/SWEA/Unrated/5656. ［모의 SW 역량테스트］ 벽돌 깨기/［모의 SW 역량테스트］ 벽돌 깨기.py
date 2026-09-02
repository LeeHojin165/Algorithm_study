from collections import deque
import copy

N, W, H, result = 0, 0, 0, []
# 벽돌을 깨는 로직
def bfs(start_row, start_col, matrix):
    queue = deque([(start_row, start_col)])
    brick_crash_cnt = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while queue:
        row, col = queue.popleft()
        brick_num = matrix[row][col]
        matrix[row][col] = 0
        brick_crash_cnt += 1
        #만약에 벽돌숫자가 1이면 자기만 0이 되고 끝남
        if brick_num != 1:
            # 벽돌 숫자가 1이 아니면 벽돌숫자-1만큼의 범위만큼 큐에 넣어야함 그리고 자신을 0으로 만듬
            for offset in range(1, brick_num):
                for i in range(4):
                    nrow = row + (dr[i] * offset)
                    ncol = col + (dc[i] * offset)
                    # col은 W row는 H
                    if 0 <= nrow < H and 0 <= ncol < W and matrix[nrow][ncol] != 0:
                        queue.append((nrow, ncol))

    return brick_crash_cnt


# 공중에 떠 있는 벽돌을 밑으로 잡아당김
def brick_drop(matrix):
    # 매트릭스 열에 있는 애들은 싹다 뽑은뒤 0을 제거하고 밑에서부터 쌓아올림
    for col in range(W):
        stack = []
        for row in range(H):
            # 0이 아닌 애들을 stack으로 집어넣고 0으로 초기화함
            if matrix[row][col] != 0:
                stack.append(matrix[row][col])
                matrix[row][col] = 0
        # 다 봤으면 index : H - 1부터 스택의 값을 쌓아올림 스택이 빌 때까지
        cur_row = H - 1
        while stack:
            matrix[cur_row][col] = stack.pop()
            cur_row -= 1


# 공을 N번 떨구는 로직을 재귀함수로 구현함
def ball_drop(ball_drop_cnt, matrix, brick_crash_cnt):
    global result
    origin_matrix = copy.deepcopy(matrix)

    if ball_drop_cnt == N:
        brick_cnt = 0
        # 벽돌의 개수
        for row in range(H):
            for col in range(W):
                if matrix[row][col] != 0:
                    brick_cnt += 1

        # for row in matrix:
        #     print(row)
        # print()
        result.append(brick_cnt)
        return

        # col은 W row는 H인것을 기억
    for col in range(W):
        # 0이 아닌 벽돌까지 간다음
        for row in range(H):
            if matrix[row][col] != 0:
                # bfs로 벽돌을 다 깬다. 벽돌을 깨면서 몇개깼는지 센다.
                brick_crash_cnt += bfs(row, col, matrix)
                break
        # 다 깨고 나면 공중에 있는 벽돌을 아래로 내려야함
        brick_drop(matrix)
        # 벽돌을 다 깼으면 다음 경우의 수로 간다.
        ball_drop(ball_drop_cnt + 1, copy.deepcopy(matrix), brick_crash_cnt)
        # 매트릭스 원상복구
        matrix = copy.deepcopy(origin_matrix)


def solve():
    # 공을 떨구는 횟수, 너비, 높이
    global N, W, H, result
    result = []
    N, W, H = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(H)]

    init_brick_cnt = 0
    # 처음에 벽돌의 갯수를 센다
    for row in range(H):
        for col in range(W):
            if matrix[row][col] != 0:
                init_brick_cnt += 1
    # print(init_brick_cnt)
    # 벽돌의 너비만큼 돌면서 모든 경우의 수를 돈다.
    # 몇만큼? 떨구는 횟수 N만큼
    ball_drop(0, matrix, 0)
    return min(result)


T = int(input())
for test_case in range(1, T + 1):
    answer = solve()
    print(f"#{test_case} {answer}")
