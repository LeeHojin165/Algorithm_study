def dfs(idx, N, cur_sum, res, is_used, board):
    if idx == N:
        res = min(cur_sum, res)
        return res
    
    for i in range(N):
        if is_used[i]:
            continue
        is_used[i] = True
        cur_sum += board[idx][i]
        if cur_sum <= res:
            res = dfs(idx + 1, N, cur_sum, res, is_used, board)
        cur_sum -= board[idx][i]
        is_used[i] = False
    return res


def solve():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    is_used = [False] * N
    return dfs(0, N, 0, float('inf'), is_used, board)
    

T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")