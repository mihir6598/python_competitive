def solve(n):
    
    if dp[n] != 0:
        return dp[n]
    dp[n] = solve(n-2) + solve(n-1)
    print (n)
    return dp[n]

if __name__ == "__main__":
    n = 10
    dp = [0 for i in range(n+1)]
    dp[1] = 2
    dp[2] = 3
    print (solve(n))