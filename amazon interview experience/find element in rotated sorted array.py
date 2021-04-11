def search(arr,l,r,n):
    if l<=r:
        
        m = (l+r)//2
        print (l,r,m)
        if arr[m] == n:
            print (m)
            return
        if n<arr[m]:
            if n>=arr[l] and n < arr[m]:
                search(arr,l,m-1,n)
            else:
                search(arr,m+1,r,n)
        else:
            if n>arr[m] and n<=arr[r]:
                search(arr,m+1,r,n)
            else:
                search (arr,l,m-1,n)
if __name__ == "__main__":
    arr = [5,6,7,1,2,3,4]
    search (arr,0,len(arr)-1,2)