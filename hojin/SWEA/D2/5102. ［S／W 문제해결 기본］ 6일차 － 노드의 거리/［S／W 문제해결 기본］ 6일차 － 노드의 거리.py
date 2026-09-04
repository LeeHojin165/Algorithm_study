from collections import deque
T = int(input())

for test_case in range(1,T+1):
    result = 0
    V, E = map(int, input().split())

    graph = [[] for i in range(V+1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    S, G = map(int, input().split())

    visited = {S}
    queue = deque([(S,0)])

    while queue:
        node, dist = queue.popleft()

        if node == G:
            result = dist
            break

        for next in graph[node]:
            if next not in visited:
                queue.append((next,dist+1))
                visited.add(next)
            

    print(f'#{test_case} {result}')