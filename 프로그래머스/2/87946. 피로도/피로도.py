from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    #k는 현재 피로도, dungeons는 필요 피로도와 소모 피로도가 2차원 배열로 주어질때
    # 탐험할 수 있는 최대 던전 수를 return하라
    # 탐험 순서에 따라 갈 수 있는 던전 수가 달라질 수 있음
    # 근데 최악의 경우가 8! = 4만 이니까 일단 해보자
    n = len(dungeons)
    
    for per in permutations(dungeons):
        cur_k = k
        cnt = 0
        #n개의 던전을 탐색
        for i in range(n):
            #i번째 던전
            dun = per[i]
            #필요 피로도
            pil = dun[0]
            #소모 피로도
            so = dun[1]
            
            if pil <= cur_k:
                cur_k -= so
                cnt += 1
        answer = max(answer,cnt)
        if answer == n:
            break
        
    return answer