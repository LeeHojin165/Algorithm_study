T = int(input())
result = 0
min_pass_processor = 0

def copy_matrix(matrix):
    return [row[:] for row in matrix]


def dfs(processors, index, matrix, n, total_cable_length,pass_processor_cnt):
    global result, min_pass_processor
    matrix = copy_matrix(matrix)
    origin_matrix = copy_matrix(matrix)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    if index == len(processors):
        #패스한 프로세스수의 최소를 갱신하면
        if pass_processor_cnt < min_pass_processor:
            min_pass_processor = pass_processor_cnt
            result = total_cable_length
            # for row in matrix:
            #     print(row)
            # print(total_cable_length)
        #같으면
        elif pass_processor_cnt == min_pass_processor:
            # for row in matrix:
            #     print(row)
            # print(total_cable_length)
            result = min(result,total_cable_length)
        return
    # index 프로세서부터 시작
    row, col = processors[index]

    # 상 하 좌 우 순서로 배열의 끝까지 가면서 프로세스나 전선이 없다면
    # 전선의 길이를 저장하면서 다음 분기로 간다.

    # 4방향중 한방향이라도 전원이 연결되면 True로 바뀐다.
    isAllConnect = False
    for dir in range(4):
        offset = 1
        cable_length = 0
        isConnect = True
        while True:
            nrow = row + dr[dir] * offset
            ncol = col + dc[dir] * offset
            if 0 <= nrow < n and 0 <= ncol < n:
                # 프로세스거나 전선이면 matrix를 원상복구 시키고 break한다.
                if matrix[nrow][ncol] != 0:
                    matrix = copy_matrix(origin_matrix)
                    # 이 방향으로는 연결할 수 없음
                    isConnect = False
                    break
                # 프로세스나 전선이 아니면
                elif matrix[nrow][ncol] == 0:
                    # 전선으로 채운다.
                    matrix[nrow][ncol] = 2
                    cable_length += 1
                    offset += 1
            else:
                break
        # 한 방향에 대해 전선을 모두 채웠으면
        if isConnect:
            isAllConnect = True
            # 다음 프로세스를 연결하러 이동
            dfs(processors, index + 1, matrix, n, total_cable_length + cable_length, pass_processor_cnt)
            matrix = copy_matrix(origin_matrix)

    # 모든 방향에 대해 전원을 연결하지 못했을 때에도 다음 프로세스로 이동해야함
    dfs(processors, index + 1, copy_matrix(origin_matrix), n, total_cable_length, pass_processor_cnt+1)


for test_case in range(1, T + 1):
    result = float('inf')
    min_pass_processor = float('inf')
    n = int(input())

    matrix = [list(map(int, input().split())) for _ in range(n)]
    processors = []
    for row in range(n):
        for col in range(n):
            # 이미 전원에 연결되어 있으면 넣지 않음
            if row == 0 or col == 0 or row == n - 1 or col == n - 1:
                continue
            if matrix[row][col] == 1:
                processors.append((row, col))

    dfs(processors, 0, matrix, n, 0,0)
    print(f"#{test_case} {result}")
