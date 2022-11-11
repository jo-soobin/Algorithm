def solution(dirs):
    result = [[0] * 11 for i in range(11)]
    x, y = 5, 5
    cnt = 0
    check = []
    for i in dirs:
        tmp = []
        first = (x, y)
        if 0 <= x <= 10 and 0 <= y <= 10:
            if i == 'U':
                x -= 1
            elif i == 'L':
                y -= 1
            elif i == 'R':
                y += 1
            else:
                x += 1
        second = (x, y)
        tmp.append(first)
        tmp.append(second)

        if tmp not in check and 0 <= x <= 10 and 0 <= y <= 10:
            if all(first != k[1] or second != k[0]  for k in check):
                check.append(tmp)

        if 0 <= x <= 10 and 0 <= y <= 10:
            result[x][y] += 1 
        else:
            if x == -1:
                x = 0
            elif y == -1:
                y = 0
            elif x == 11:
                x = 10
            else:
                y =10

    return len(check)