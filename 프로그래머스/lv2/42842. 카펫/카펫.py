def solution(brown, yellow):  # 근의 공식 활용
    x = (brown + 4 + ((brown + 4) ** 2 - 16 * (brown + yellow)) ** 0.5) / 4
    y = (brown + yellow) / x

    return [x, y]