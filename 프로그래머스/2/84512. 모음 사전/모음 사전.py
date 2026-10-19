from collections import deque


def bfs(word, moem):
    # 현재 단어와 순서 정수를 큐에 넣음
    queue = deque([("A", 1)])

    while queue:
        cur_word, cnt = queue.popleft()

        #print(cur_word, cnt)
        if cur_word == word:
            return cnt
        # 길이가 5보다 작으면
        if len(cur_word) < 5:
            # A를 붙인다
            queue.append((cur_word + "A", cnt + 1))


        elif len(cur_word) == 5:
            for i in range(5):
                # 마지막 글자를 비교했을때
                if cur_word[4] == moem[i]:
                    if i < 4:
                        cur_word = cur_word[:4] + moem[i+1]
                        queue.append((cur_word, cnt + 1))
                        break
                    # U이면
                    elif i == 4:
                        End = False
                        #마지막 글자가 U이면
                        while True:
                            #마지막 글자가 U임
                            if cur_word[-1] == moem[4]:
                                cur_word = cur_word[:len(cur_word)-1]
                            #마지막 글자가 U가 아님
                            else:
                                for j in range(5):
                                    if cur_word[-1] == moem[j]:
                                        #print(cur_word)
                                        cur_word = cur_word[:len(cur_word)-1] + moem[j+1]
                                        End = True
                                        break
                            if End:
                                break
                        queue.append((cur_word, cnt + 1))
                        break

    # 다 돌았는데 못찾으면 -1 반환
    return -1


def solution(word):
    answer = 0
    moem = ['A', 'E', 'I', 'O', 'U']

    answer = bfs(word, moem)
    return answer

solution("AAAE")