def solution(str1):
    n = len(str1)
    dp = [[0 for i in range(n+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if str1[i-1] == str1[j-1]:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            print (dp)

    print (dp[n-1][n])

if __name__ == "__main__":
    str1 = "aabebcdd"
    solution(str1)