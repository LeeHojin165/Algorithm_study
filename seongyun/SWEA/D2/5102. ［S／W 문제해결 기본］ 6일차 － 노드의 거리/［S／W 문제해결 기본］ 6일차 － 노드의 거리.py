from collections import deque

def solve():
    v, e = map(int, input().split())
    edge = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)
    s, g = map(int, input().split())

    q = deque([s])
    visited = [False] * (v + 1)
    visited[s] = True

    level = 0
    while q:
        level += 1
        length = len(q)

        for _ in range(length):
            cur = q.popleft()

            for node in edge[cur]:
                if not visited[node]:
                    q.append(node)
                    visited[node] = True
                    if node == g:
                        return level

    return 0

T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")