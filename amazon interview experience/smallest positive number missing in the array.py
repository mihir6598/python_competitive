def solve(arr):
    l = 0
    r = len(arr)-1

    while (l<=r):
        if arr[l]<0 and arr[r]>=0:
           arr[l],arr[r] = arr[r],arr[l]
        if arr[l]>=0:
            l+=1
        if (arr[r]<0):
            r -= 1

        arr[l],arr[r] = arr[r],arr[l]
    print (l)
    print (arr)
    for i in range(l):
        if abs(arr[i])<l:
            arr[abs(arr[i])] = -1*abs(arr[abs(arr[i])])
    for i in range(1,l):
        if arr[i]>0:
            return i
    return -1






if __name__ == "__main__":
    arr = [1, 1, 0, -1, -2]
    print (solve(arr))