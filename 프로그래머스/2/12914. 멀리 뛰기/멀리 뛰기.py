def solution(n):

    dp=[0]* 2002
    dp[1]=1
    dp[2]=2
    dp[3]=3
    if(n==1 or n==2 or n==3):
        return dp[n]
    else:
        for i in range(3,n+1):
            dp[i]= dp[i-1]+dp[i-2]
    return dp[n]%1234567