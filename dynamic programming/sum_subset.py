# DP-18
def answer(arr):
    n = len(arr)
    s = int(sum(arr))
    dp = [[False for j in range(int((s/2)+1))]for i in  range(n+1)]

    for i in range(n+1):
        dp[i][0] = True
    print (dp)
    for i in range(1,len(arr)+1):
        for j in range(int((s/2)+1)):
        
            if j>= arr[i-1]:
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-arr[i-1]])
                print (dp[i][j])
            else:
                dp[i][j] = dp[i-1][j]
    print (dp)

if __name__ == "__main__":
    # arr = list(map(int,input().split(" ")))
    arr = [2,3,10,1]
    answer(arr)
