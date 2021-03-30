def solve_low(arr,n,l,r):
    if l<=r:
        m = int((l+r)/2)
        if arr[m] == n and (m==0 or arr[m-1] != n):
                return m
        elif arr[m]<n:
            return solve_low(arr,n,m+1,r)
        else:
            return solve_low(arr,n,l,m-1)
    else:
        return -1
def solve_max(arr,n,l,r):
    if l<=r:
        m = int((l+r)/2)
        if arr[m] == n and (m==len(arr)-1 or arr[m+1] != n):
                return m
        elif arr[m]>n:
            return solve_max(arr,n,l,m-1)
        else:
            return solve_max(arr,n,m+1,r)
    else:
        return -1
if __name__ == "__main__":
    arr = [3,3,3,3,3,3,3]
    print (solve_low(arr,3,0,len(arr)-1))
    print (solve_max(arr,3,0,len(arr)-1))