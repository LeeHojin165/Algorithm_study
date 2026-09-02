T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    result = 0
    board = [list(map(int, input())) for _ in range(n)]
    middle = int(n/2)
    for row in range(n):
        for col in range(n):
            if abs(middle - row) + abs(middle - col) <= middle:
                result += board[row][col]

    print(f'#{test_case} {result}')