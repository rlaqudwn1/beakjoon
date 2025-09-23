def solution(land):
    answer = 0
    up=0
    for i in range(1,len(land)):
        for j in range(4):
            for k in range(4):
                if(k!=j):
                    up=max(up,land[i-1][k])
            
            land[i][j]+=up
            up=0
            
                
    
    return max(land[-1])