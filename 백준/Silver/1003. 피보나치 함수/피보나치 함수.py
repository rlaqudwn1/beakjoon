t= int(input())
for _ in range(t):
    n = int(input())
    if(n==0):
        print("1 0")
    else:
        dp = [[0,0] for _ in range (n+2)]
        dp[0] = [1,0]
        dp[1] = [0,1]
        for i in range(2,n+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]
        print(f"{dp[n][0]} {dp[n][1]}")
# 피보나치 수열로 단순 0과 1의 개수를 구하는 그리디 방식으로 생각했으나
# 타임 오버 된 후 다이나믹 프로그래밍 방법을 참고
    
