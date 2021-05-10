def solve(arr,time):
    hash = {}
    time = time - 30
    for i in range(len(arr)):
        if arr[i] not in hash:
            hash[arr[i]] = i
    m = 0
    for i in range(len(arr)):
        temp = time - arr[i]
        if temp in hash:
            if max(temp,arr[i])>m:
                m = max(temp,arr[i])
                ans = (i,hash[temp])
    return ans

if __name__ == "__main__":
    arr = [1, 10, 25, 35, 60]
    time = 90
    print (solve(arr,time))