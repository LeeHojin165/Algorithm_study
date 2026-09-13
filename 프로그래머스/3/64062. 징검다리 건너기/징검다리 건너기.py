from collections import deque

def solution(stones, k):
    dq = deque()
    answer = 1e9

    for i in range(len(stones)):
        while dq and stones[dq[-1]] <= stones[i]: dq.pop()
        dq.append(i)
        if dq[0] <= i - k: dq.popleft()
        if i >= k - 1:
            max_value = stones[dq[0]]
            answer = min(answer, max_value)
    return answer


"""
# 시간 초과 코드
def solution(stones, k):
    answer = 1e9
    for i in range(0, len(stones) - k + 1):
        max_value = max(stones[i : i+k])
        if max_value < answer:answer = max_value
    return answer
"""