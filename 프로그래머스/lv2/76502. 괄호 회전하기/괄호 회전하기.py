def solution(s):
    answer = 0
    arr = [s]
    for i in range(len(s)-1):
        arr.append(arr[-1][1:]+arr[-1][0])
    
    for i in arr:
        if check(i):
            answer+=1
    
    return answer

def check(s):
    stack = [s[0]]
    for i in s[1:]:
        if len(stack) == 0:
            stack.append(i)
        elif i == ')' and stack[-1]=='(':
            del stack[-1]
        elif i==']' and stack[-1]=='[':
            del stack[-1]
        elif i=='}' and stack[-1]=='{':
            del stack[-1]
        else:
            stack.append(i)
    if len(stack)==0:
        return True
    
    return False