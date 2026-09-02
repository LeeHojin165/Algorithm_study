import heapq

def solve():
    N = int(input())
    board = []
    for _ in range(N):
        board += list(map(int, input().split()))

    INF = float('inf')
    dist = [INF] * (N * N)
    dist[0] = board[0]
    pq = [(board[0], 0)]

    while pq:
        cur_cost, u = heapq.heappop(pq)

        if cur_cost > dist[u]:
            continue

        if u % N != N - 1:
            next_cost = cur_cost + board[u + 1]

            if next_cost < dist[u + 1]:
                dist[u + 1] = next_cost
                heapq.heappush(pq, (next_cost, u + 1))
        if u < N * (N - 1):
            next_cost = cur_cost + board[u + N]

            if next_cost < dist[u + N]:
                dist[u + N] = next_cost
                heapq.heappush(pq, (next_cost, u + N))
    
    return dist[(N * N - 1)]

T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")