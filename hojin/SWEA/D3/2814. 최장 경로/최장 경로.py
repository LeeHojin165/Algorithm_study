T = int(input())

def backtrack(start,matrix,visited,length):

    global result
    #print(start, length)
    if not matrix[start]:
        result = max(result,length)
        return
    else:
        #모든 노드를 방문함
        all = True
        # 만약에 갈 노드가 있어도 남은 노드가 다 방문했으면 종료
        for nxt in matrix[start]:
            # 모든 노드에 방문함?
            if not visited[nxt]:
                # 안 했음? 그러면 False임
                all = False

        if all:
            result = max(result,length)
            return

    for nxt in matrix[start]:

        if not visited[nxt]:
            visited[nxt] = True
            backtrack(nxt,matrix,visited,length+1)
            visited[nxt] = False

for tc in range(1,T+1):
    result = 0
    n, m = map(int, input().split())
    matrix = [[] for _ in range(n+1)]

    for _ in range(m):
        x, y = map(int, input().split())
        matrix[x].append(y)
        matrix[y].append(x)


    for i in range(1,n+1):
        visited = [False] * (n+1)
        visited[i] = True
        backtrack(i,matrix,visited,1)



    print(f'#{tc} {result}')