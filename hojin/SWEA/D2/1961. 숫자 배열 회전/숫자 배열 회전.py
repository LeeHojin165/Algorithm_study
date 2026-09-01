# def rotate_90(arr, n):
#     result = [[0] * n for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             result[j][n - i - 1] = arr[i][j]

#     return result

def rotate_90(arr, n):
    result = [row for row in zip(*arr[::-1])]

    return result


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    original_arr = [list(map(int, input().split())) for _ in range(n)]

    arr_90 = rotate_90(original_arr, n)
    arr_180 = rotate_90(arr_90, n)
    arr_270 = rotate_90(arr_180, n)

    print(f"#{test_case}")

    for i in range(n):
        result_90 = "".join(map(str, arr_90[i]))
        result_180 = "".join(map(str, arr_180[i]))
        result_270 = "".join(map(str, arr_270[i]))

        print(result_90, result_180, result_270)