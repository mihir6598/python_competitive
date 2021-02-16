def solution(arr):
    n = len(arr)
    dp = [0 for i in range(n)]
    dp[0] = arr[0]
    dp[1] = max(arr[1],arr[0])
    for i in range(2,n):
        dp[i] = max(arr[i]+dp[i-2],dp[i-1])
    print (dp[n-1])


if __name__ == "__main__":
    arr = [5,3,4,11,2]
    solution(arr)