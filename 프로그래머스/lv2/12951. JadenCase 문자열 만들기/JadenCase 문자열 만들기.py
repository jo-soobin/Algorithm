def solution(s):
    new_word = ''
    word = s.split(' ')
    for i in range(len(word)):
        word[i] = word[i].capitalize()
    new_word = ' '.join(word)
    return new_word
