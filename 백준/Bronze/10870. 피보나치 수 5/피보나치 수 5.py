# 피보나치 n번째 피보나치 수를 출력하도록 해라.

n=int(input())

dp = [0 for i in range (n+2)]

dp[0]=0
dp[1]=1

for i in range(2,n+2):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])