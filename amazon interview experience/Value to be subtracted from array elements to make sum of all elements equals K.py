from collections import defaultdict
def return_sum(arr,n):
    ans = 0
    for i in arr:
        if i > n:
            ans = ans + i - n
    return ans

def solve2(arr,k,l,r):
    if l < r:
        mid = (l + r)//2
        temp = return_sum(arr,mid)
        if temp  == k:
            return mid
        if temp > k:
            solve2(arr,k,mid+1,r)
        if temp<k:
            solve2(arr,k,l,mid-1)
    return -1
def solve(arr,k):
    arr.sort()
    l = 0
    r = arr[-1]
    return solve2(arr,k,l,r)

if __name__ == "__main__":
    arr = [1, 1, 2, 2]
    k = 1
    print (solve(arr,k))