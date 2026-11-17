# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
 
 
def dfs(y, x, worked, now_len):
    global max_len
 
    # 다음에 갈 후보들
    wait = []
    # 현재 위치에서 4개 방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 인덱스 넘어가는 곳은 못감
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        # 이미 갔던곳은 못감
        if visited[ny][nx] == 1:
            continue
        # 더 높은 곳으로는 못감 (이미 공사를 한 경우)
        if arr[ny][nx] >= arr[y][x] and worked > 0:
            continue
        # 공사 못하는 높이는 못감
        if arr[ny][nx] - arr[y][x] >= K:
            continue
        # 공사를 할 수 있는 경우 (아직 공사 안 했고, 나보다 높거나 같은 지점)
        if 0 <= arr[ny][nx] - arr[y][x] < K:
            wait.append((ny, nx, arr[ny][nx] - arr[y][x] + 1))
            continue
        # 그냥 갈 수 있는 경우 (나보다 낮은 지점)
        wait.append((ny, nx, 0))
 
    # 종료 조건
    # 4방향 탐색했을 때 더 이상 갈 곳이 없음
    if len(wait) == 0:
        max_len = max(now_len, max_len)
        return
 
    # 재귀
    for ny, nx, need_work in wait:
        # 갈 곳을 방문처리
        visited[ny][nx] = 1
 
        # 이동
        if need_work:
            # 최소 깎아야 하는 높이부터 K까지 깎음
            for i in range(need_work, K + 1):
                temp = arr[ny][nx]
                arr[ny][nx] -= i
                dfs(ny, nx, 1, now_len + 1)
                arr[ny][nx] = temp
        else:
            dfs(ny, nx, worked, now_len + 1)
 
        # 갔다는 표시 풀어줌
        visited[ny][nx] = 0
 
 
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
 
    arr = []
    max_n = 0
    s_point = []
    for y in range(N):
        row = list(map(int, input().split()))
        for x in range(N):
            if row[x] > max_n:
                max_n = row[x]
                s_point = []
                s_point.append((y, x))
            elif row[x] == max_n:
                s_point.append((y, x))
        arr.append(row)
 
    visited = [[0] * N for _ in range(N)]
    max_len = 0
 
    for y, x in s_point:
        visited[y][x] = 1
        dfs(y, x, 0, 1)
        visited[y][x] = 0
 
    print(f"#{tc} {max_len}")