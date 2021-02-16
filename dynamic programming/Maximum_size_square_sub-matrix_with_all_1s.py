def solution(arr):
    n = len(arr)
    m = len(arr[0])

    dp = arr
    ans = 0
    for i in range(1,n):
        for j in range(1,m):
            if min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])>0 and dp[i][j] == 1:
                dp[i][j] = dp[i-1][j-1] + 1
                ans = max(ans,dp[i][j])
                print (dp)
    print (ans)

if __name__ == "__main__":
    arr = M = [[0, 1, 1, 0, 1], 
    [1, 1, 0, 1, 0], 
    [0, 1, 1, 1, 0], 
    [1, 1, 1, 1, 0], 
    [1, 1, 1, 0, 1], 
    [0, 1, 0, 0, 0]] 
    solution(arr)