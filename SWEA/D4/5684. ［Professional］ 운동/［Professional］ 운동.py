T = int(input())
INF = 1e9
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        s, e, c = map(int, input().split())
        dist[s][e] = c

    # 플로이드-워셜
    for k in range(1, N + 1):
        dist_k = dist[k]
        for i in range(1, N + 1):
            dist_i = dist[i]
            dik = dist_i[k]
            if dik == INF: continue
            for j in range(1, N + 1):
                new_dist = dik + dist_k[j]
                if new_dist < dist_i[j]:
                    dist_i[j] = new_dist
    answer = min(dist[i][i] for i in range(1, N + 1))

    if answer == INF:
        answer = -1
    print(f'#{tc} {answer}')
