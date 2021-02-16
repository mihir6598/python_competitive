def solution(a,t,e,x):
    n = len(a[0])
    dp = [[0 for i in range(n)] for j in range(2)]
    dp[0][0] = e[0]+a[0][0]
    dp[1][0] = e[1]+a[1][0]
    for i in range(1,n):
        dp[0][i] = min(dp[0][i-1]+a[0][i],dp[1][i-1]+a[0][i]+t[1][i])
        dp[1][i] = min(dp[1][i-1]+a[1][i],dp[0][i-1]+a[1][i]+t[0][i])
    
    print (min(dp[0][n-1]+x[0],dp[1][n-1]+x[1]))

if __name__ == "__main__":
    a = [[4, 5, 3, 2],
        [2, 10, 1, 4]]
    t = [[0, 7, 4, 5],
        [0, 9, 2, 8]]
    e = [10, 12]
    x = [18, 7]
    solution(a,t,e,x)