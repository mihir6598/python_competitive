def solution(arr,n,m):
    # dp = [[0 for i in range(n)] for j in range(j)]
    dp = arr
    for i in range(1,n):
        for j in range(i+1):
            print (dp)
            if j == 0:
                dp[i][j] = dp[i][j] + dp[i-1][j]
            elif j == i:
                dp[i][j] = dp[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j] + dp[i-1][j-1], dp[i][j] +dp[i-1][j])
    print max(dp[n-1])



if __name__ == "__main__":
    arr = [[1, 0, 0], 
        [4, 8, 0], 
       [1, 5, 3]] 
    solution(arr,3,3)