def solve(t,s,face):
    global throw
    if s<0:
        return 0
    if t == throw and s != 0:
        return 0
    if t == throw and s == 0:
        return 1
    if dp[throw-t-1][s] != -1:
        return dp[throw-t-1][s]
    if dp[t][s] != -1:
        return dp[t][s]
    ans = 0
    for i in range(1,face+1):
        ans += solve(t+1,s-i,face)
        
    dp[t][s] = ans    
    return dp[t][s]
if __name__ == "__main__":
    throw = 6
    s = 36
    face = 6 
    dp = [[-1 for i in range(s+1) ] for j in range(throw+1)]
    print (solve(0,s,face))
    