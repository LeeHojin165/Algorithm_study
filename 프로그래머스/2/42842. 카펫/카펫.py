def solution(brown, yellow):
    answer = []
    
    #가로를 a 세로를 b 라고할때
    #가로의 범위는 brown // 2 - 1
    #세로의 범위는?
    for a in range(3,brown // 2):
        b = (brown+4) //2 - a
        if a*b == brown+yellow and a>= b:
            answer.append(a)
            answer.append(b)
            break
            
        
    
    
    return answer