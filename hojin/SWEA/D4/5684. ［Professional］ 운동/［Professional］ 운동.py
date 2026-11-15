from heapq import heappush, heappop

T = int(input())
INF = float('inf')
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, c = map(int, input().split())
        adj[s].append((e, c))
    best = INF
    for s in range(1, n + 1):
        dist = [INF] * (n + 1)
        dist[s] = 0
        h = [(0, s)]
        while h:
            d, u = heappop(h)
            if d >= best:
                break
            if d > dist[u]:
                continue
            for v, c in adj[u]:
                nd = d + c
                if nd >= best:
                    continue
                if v == s:
                    best = nd
                    continue
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(h, (nd, v))
    print(f"#{tc} {best if best != INF else -1}")