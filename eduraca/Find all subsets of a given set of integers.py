def solve(arr,p,n,l):
    if p == n:
        print ("in")
        final.append(l)
        return
    solve(arr,p+1,n,l)
    solve(arr,p+1,n,l+[arr[p]])



if __name__ == "__main__":
    arr = [2,3,4,1,9]
    final = []
    temp = []
    solve(arr,0,len(arr),temp)
    print (final)