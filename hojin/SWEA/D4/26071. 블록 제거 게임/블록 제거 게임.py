T = int(input())
result = 0
def dfs(blocks, cur_score):
    global result

    if not blocks:
        result = max(result, cur_score)
        return
    n = len(blocks)
    for idx in range(len(blocks)):
        temp = blocks[idx]
        #점수 계산 먼저
        score = 0
        left = idx - 1
        right = idx + 1

        if n == 1:
            score += blocks[idx]
        else:
            if left >= 0 and right < n:
                score += blocks[left] * blocks[right]
            else:
                if left < 0:
                    score += blocks[right]
                elif right >= n :
                    score += blocks[left]


        #점수계산후 해당 블럭 제거
        blocks.pop(idx)
        dfs(blocks,cur_score+score)
        #원상복귀
        blocks.insert(idx,temp)

for test_case in range(1,T+1):
    result = 0
    n = int(input())
    blocks = list(map(int, input().split()))

    dfs(blocks, 0)
    print(f'#{test_case} {result}')