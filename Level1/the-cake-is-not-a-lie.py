def solution(s):
    max = 1
    
    for i in range(len(s)):
        length = len(s) / (i + 1)
        succ = True
        
        for j in range(len(s)):
            if s[j] != s[j % length]:
                succ = False
                break

        if succ:
            max = i + 1

    return max