def solution(array, commands):
    answer = []
    for i in commands:
        new_arr = array[i[0]-1:i[1]]
        new_arr.sort()
        answer.append(new_arr[i[2]-1])
    return answer
        