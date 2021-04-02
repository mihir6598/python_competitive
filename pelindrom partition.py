def check(s):
    return s==s[::-1]
def solve(s,i,j):

    if i == j:
        dp[i][j] = 0
        return 0
    
    if i == j-1:
        dp[i][j] = 0
        return 0

    if dp[i][j] != 10:
        return dp[i][j]

    for k in range(i+1,j+1):
        if check(s[i:k]):
            dp[i][k] = 0
            dp[k][j] = solve(s,k,j)
            if k != j:
                dp[i][j] = min(1+dp[i][k] + dp[k][j],dp[i][j])
            print (i,j,k,dp[i][j],dp[i][k],dp[k][j]) 
    # print (dp)
    return dp[i][j]
if __name__ == "__main__":
    s = "aabvf"
    dp = [[10 for i in range(len(s)+1)] for j in range(len(s)+1)]
    print (solve(s,0,len(s)))