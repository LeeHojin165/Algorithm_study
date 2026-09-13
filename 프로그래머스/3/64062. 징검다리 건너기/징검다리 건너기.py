# 시간초과
"""
def solution(stones, k):
    answer = 1e9
    for i in range(0, len(stones) - k + 1):
        max_value = max(stones[i : i+k])
        if max_value < answer : answer = max_value
        print(max_value, stones[i : i+k])
    return answer
"""

def solution(stones, k):
    left = 0
    right = max(stones)+1

    def compare(mid):
        return any(len(i)>=k for i in "".join(["T" if i>mid else "F" for i in stones]).split("T"))

    while left<right:
        mid = (left+right)//2
        if compare(mid):
            right = mid
        else:
            left = mid + 1

    return right