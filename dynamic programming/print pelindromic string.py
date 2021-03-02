
def longestPalindrome(s: str) -> str:
    res = ""
    n = len(s)
    reverse = s[::-1]
    print (reverse)
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    m = 0
    for i in range(1,n+1):
        for j in range(1,n+1-i-1):
            if s[j-1] == reverse[i-1]:
                dp[i][j] = dp[i][j-1] + 1
                if dp[i][j]>m:
                    m = dp[i][j]
                    ans = j
            else:
                dp[i][j] = dp[i-1][j]
        print (dp)
    
    res = s[ans-m:ans]
    return res

output = longestPalindrome("aacabdkacaa")
print (output)