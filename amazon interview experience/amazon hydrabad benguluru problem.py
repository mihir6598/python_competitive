def solveutil(arr,i,h,b,n,ans):
    if h<n/2 and b<n/2:
        ans += min(arr[i][0] + solveutil(arr,i+1,h+1,b,n,ans),arr[i][1] + solveutil(arr,i+1,h,b+1,n,ans))
    elif b<n/2:
        ans += arr[i][1] + solveutil(arr,i+1,h,b+1,n,ans)
    elif h<n/2:
        ans += arr[i][0] + solveutil(arr,i+1,h+1,b,n,ans)
    return ans
        

def solve2(arr):
    arr.sort(key=lambda x : max(x[0],x[1]),reverse=True)
    print (arr)
    h = 0
    b = 0
    n = len(arr)
    ans = 0
    for i in arr:
        if h<n/2 and b<n/2:
            if i[0]>i[1]:
                ans = ans + i[1]
                b += 1
            else:
                ans = ans + i[0]
                h += 1
        elif h<n/2:
                ans = ans + i[0]
                h += 1
        elif b<n/2:
            ans = ans + i[1]
            b += 1
    return ans
        

def solve(arr):
    n = len(arr)
    ans = 0
    i = 0
    h = 0
    b = 0
    print (solveutil(arr,i,h,b,n,ans))
    print (solve2(arr))

if __name__ == "__main__":
    arr = [ [100,90], [90,80], [80,70], [60,1],[4,2], [5,3]]
    solve(arr)