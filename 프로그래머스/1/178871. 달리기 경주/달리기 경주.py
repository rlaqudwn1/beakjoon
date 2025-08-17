
def solution(players, callings):
    answer=[]
    pos = {name : i for i,name in enumerate (players)} # 튜플형
    for name in callings:
        i=pos[name]
        j=i-1
        front=players[j]
        players[i],players[j]=players[j],players[i]
        
        pos[name]=j
        pos[front]=i
    return players
