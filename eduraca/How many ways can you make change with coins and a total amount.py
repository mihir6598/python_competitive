def solve(arr,n):
    dp = [0 for i in range(n+1)]
    for i in range(1,len(arr)+1):
        for j in range(1,n+1):
            if j == arr[i-1]:
                dp[j] = dp[j] + 1
            if j > arr[i-1]:
                dp[j] = dp[j] + dp[j-arr[i-1]]
    return (dp[n])

if __name__ == "__main__":
    coins = [1,2,5]
    n = 7
    print (solve(coins,7))