cnt = 0


def dfs(numbers, target, val, index):
    global cnt
    n = len(numbers)

    #print(val)
    if val == target and index == n:
        cnt += 1
        return
    
    if index < n:
        num = numbers[index]
        # 더하거나
        dfs(numbers, target, val + num, index + 1)
        # 빼거나
        dfs(numbers, target, val - num, index + 1)


def solution(numbers, target):
    answer = 0
    n = len(numbers)
    dfs(numbers, target, 0, 0)
    answer = cnt
    return answer
