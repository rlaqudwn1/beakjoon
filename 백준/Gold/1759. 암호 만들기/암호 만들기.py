L,C = map(int, input().split())
mo =['a','e','i','o','u']
code = list(input().split())
code.sort()
arr=[]

def inspect(arr):
    mo_count=0
    ja_count=0
    for i in arr:
        if i in mo:
            mo_count+=1
        else:
            ja_count+=1
    if(mo_count>=1 and ja_count>=2):
        return True
    else:
        return False 
def dfs(depth,start):
    if depth ==L and inspect(arr):
        print(''.join(arr))
        return
    for i in range(start,C):
        arr.append(code[i])
        dfs(depth+1,i+1)
        arr.pop()


dfs(0,0)