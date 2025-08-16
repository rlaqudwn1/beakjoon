def solution(t, p):
    t_len=len(t)
    p_len=len(p)
    start=0
    answer = 0

    for i in range(p_len,t_len+1):
        sep=t[start:i]
        if(int(sep)<=int(p)):
            answer+=1
        start+=1
    return answer