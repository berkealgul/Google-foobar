def solution(s):
    max = 1
    sl = len(s)

    for i in range(sl):
        sub_len = sl / (i + 1)
        succ = True

        for j in range(sl):
            if s[j] != s[j % sub_len]:
                succ = False
                break

        if succ:
            max = i + 1

    return max
