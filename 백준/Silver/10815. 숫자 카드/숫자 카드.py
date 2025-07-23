N = int(input())

A = list(map(int, input().split()))

M = int(input())

B = list(map(int, input().split()))
A.sort()
for i in  range(M):
    left=0
    right=len(A)-1
    correct=False
    while(left<=right):
        mid=(left+right)//2
        if(A[mid]<B[i]):
            left=mid+1
        if(A[mid]>B[i]):
            right=mid-1
        if(A[mid]==B[i]):
            correct=True
            break
    if correct:
        print("1")
    else:
        print("0")