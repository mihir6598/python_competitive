def solve(arr,n):
    ans = n*(n+1)/2
    return ans - sum(arr)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    print (solve(arr,10))