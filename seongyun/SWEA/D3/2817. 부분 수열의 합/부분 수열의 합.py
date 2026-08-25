def dfs(idx, nums, N, K, k, cnt):
    if k == K:
        return cnt + 1
    elif k > K:
        return cnt
    
    if idx == N:
        return cnt
    
    cnt = dfs(idx + 1, nums, N, K, k + nums[idx], cnt)
    cnt = dfs(idx + 1, nums, N, K, k, cnt)
    return cnt


def solve():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    
    ans = dfs(1, nums, N, K, nums[0], 0)
    ans = dfs(1, nums, N, K, 0, ans)
    return ans
    

T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solve()}")