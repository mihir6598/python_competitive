# https://www.geeksforgeeks.org/maximum-tip-calculator-2/

def dpUtil(a,b,x,y,n,dp,i):
    print (i,x,y)
    if i>= n:
        return
    if dp[i][x][y] != 0:
        return 
    
    if x == 0:
        dpUtil(a,b,x,y-1,n,dp,i+1)
        if i == n-1:
            dp[i][x][y] = b[i]
        else:
            dp[i][x][y] = dp[i+1][x][y-1] + b[i]
        return
    if y == 0:
        dpUtil(a,b,x-1,y,n,dp,i+1)
        if i == n-1:
            dp[i][x][y] = a[i]
        else:
            dp[i][x][y] = dp[i+1][x-1][y] + a[i]
        return 
    
    
    
    
    dpUtil(a,b,x-1,y,n,dp,i+1)
    dpUtil(a,b,x,y-1,n,dp,i+1)
    if i == n-1:
        dp[i][x][y] = max(a[i],b[i])
    else:
        dp[i][x][y] = max(dp[i+1][x][y-1] + b[i],dp[i+1][x-1][y] + a[i])
    

def solve(a,b,x,y):
    n = len(a)
    dp = [[[0 for i in range(y+1)]for j in range(x+1)]for k in range(n)]
    
    dpUtil(a,b,x,y,n,dp,0)
    
    return dp[0][x][y]

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [5, 4, 3, 2, 1]
    x = 3
    y = 3
    
    print (solve(a,b,x,y))