
def solve(arr):
    l = 0
    n = len(arr)
    r = n - 1

    while (l<=r):
        if arr[l]>=0 and arr[r]<0:
            arr[l],arr[r] = arr[r],arr[l]
        if arr[l]<0:
            l = l + 1
        if arr[r]>=0:
            r = r - 1
        
        print (l,r)
        print (arr)
    return l

if __name__ == "__main__":
    arr = [-12,-11,-13,-5,6,-7,-5,-3,-6]
    print (solve(arr))