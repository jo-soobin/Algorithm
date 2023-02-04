def solution(s):
    answer = ''
    
    words = s.split(' ') # list형태로 저장
    
    for i in range(len(words)):
        words[i] = words[i].capitalize()
        
    answer = ' '.join(words)
    
    return answer