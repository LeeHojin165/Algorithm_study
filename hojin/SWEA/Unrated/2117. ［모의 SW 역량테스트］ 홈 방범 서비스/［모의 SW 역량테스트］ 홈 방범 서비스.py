T = int(input())


def cristal(start_i, start_j, k, matrix, n):
    local_house_cnt = 0
    for h in range(k):
        tup = (start_i - h, start_i + h)
        if h == 0:
            tup = [start_i]

        for i in tup:
            for j in range(start_j - (k - 1) + h, start_j + (k - 1) - h + 1):
                if 0 <= i < n and 0 <= j < n:
                    local_house_cnt += matrix[i][j]

    return local_house_cnt


def solve():
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    max_val = 0
    house_cnt = 0
    # 도시에 집이 몇개가 있는지 센다
    for row in matrix:
        house_cnt += sum(row)
    k = 1
    
    while k ** 2 + (k - 1) ** 2 < house_cnt * m:
        for i in range(n):
            for j in range(n):
                # k범위의 집 갯수를 센다
                local_house_cnt = cristal(i, j, k, matrix, n)
                # 그때 손해를 보지 않으면 k를 최댓값 갱신
                if local_house_cnt * m - (k ** 2 + (k - 1) ** 2) >= 0:
                    max_val = max(local_house_cnt, max_val)
        k += 1
    return max_val


for test_case in range(1, T + 1):
    result = solve()
    print(f'#{test_case} {result}')
