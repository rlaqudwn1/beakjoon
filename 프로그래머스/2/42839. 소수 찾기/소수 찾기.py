# 숫자 조합
# 함수	중복 허용 여부	순서 고려 여부
# permutations	불가능	가능
# combinations	불가능	불가능
# product	가능	가능
# combinations_with_replacement	가능	불가능
from itertools import permutations
def find_pn(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def solution(numbers):
    arr=set()
    strs=[]
    for i in numbers:
        strs.append(i)
    
    for j in range(1,len(strs)+1):
        for i in permutations(strs,j):
            num=''
            for k in i:
                num +=k
            arr.add(int(num))
    answer=0
    for i in arr:
        if i>1 and find_pn(i):
            answer+=1
            
    return answer