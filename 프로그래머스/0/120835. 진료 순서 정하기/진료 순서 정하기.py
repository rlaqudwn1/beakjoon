def solution(emergency):
    test=0
    answer=[0]*len(emergency)
    patients=sorted(emergency,reverse=True)
    for i in range(len(patients)):
        test=emergency.index(patients[i])
        answer[test]=i+1
    return answer