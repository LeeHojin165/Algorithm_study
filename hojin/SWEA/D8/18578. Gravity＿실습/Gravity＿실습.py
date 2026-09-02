T = int(input())

for test_case in range(1, T + 1):
    result = 0

    N = int(input())
    W = N
    H = 100

    matrix = [[0] * W for _ in range(H)]
    boxes_height = list(map(int, input().split()))

    for i in range(N):
        row = 99
        for _ in range(boxes_height[i]):
            matrix[row][i] = 1
            row -= 1

    for row in range(H):
        if sum(matrix[row]) == 0:
            continue
        else:
            # 스택에 원래 인덱스를 담는다.
            stack = []
            for col in range(W):
                if matrix[row][col] != 0:
                    stack.append(col)
                    # 이거 0으로 바꾸는거 굳이긴 함
                    matrix[row][col] = 0
            cur_col = W - 1
            # 끝까지 다 돌았으면 스택이 빌때까지 cur_col을 W-1부터 1씩 줄임
            while stack:
                drop_diss = cur_col - stack.pop()
                result = max(drop_diss, result)
                cur_col -= 1

    # for r in matrix:
    #     print(r)

    print(f'#{test_case} {result}')
