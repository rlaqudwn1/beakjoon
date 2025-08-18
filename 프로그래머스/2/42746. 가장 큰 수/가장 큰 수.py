from functools import cmp_to_key

def compare(x,y):
    a= x+y
    b= y+x
    if a>b:
        return -1
    elif b>a:
        return 1
    else:
        return 0
def solution(numbers):
    A=list(map(str, numbers))
    A.sort(key=cmp_to_key(compare))
    answer = ''.join(A)
    
    return "0" if answer[0] == "0" else answer