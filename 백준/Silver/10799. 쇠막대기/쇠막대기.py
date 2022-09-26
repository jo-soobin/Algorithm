stk = list(input())
answer = 0
lst = []

for i in range(len(stk)):
    if stk[i] == '(':
        lst.append('(')

    else:
        if stk[i-1] == '(': 
            lst.pop()
            answer += len(lst)

        else:
            lst.pop() 
            answer += 1 

print(answer)