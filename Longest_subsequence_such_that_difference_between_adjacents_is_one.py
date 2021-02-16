# https://docs.google.com/spreadsheets/d/1hcmTwgK6xZLqmh5W1T5I6cBKifvIMKhwz6qwyqygONE/edit#gid=0
# Longest subsequence such that difference between adjacents is one
def solution(arr):
    n = len(arr)
    dp = [1 for i in range(n)]

    for i in range(1,n):
        for j in range(i):
            if abs(arr[i]-arr[j])==1:
                dp[i] = max(dp[j]+1,dp[i])
    print (dp[n-1])

if __name__ == "__main__":
    arr = [1, 2, 3, 2, 3, 7, 2, 1]
    solution(arr)