# https://www.geeksforgeeks.org/a-product-array-puzzle-set-3/
def solve(arr):
    left = [1]*len(arr)
    for i in range(len(arr)-1):
        if i == 0:
            mul = arr[i]
        else:
            mul = mul * arr[i]
        left[i+1] = mul
    right = [1]*len(arr)
    
    for i in range(len(arr)-1,0,-1):
        if i == len(arr)-1:
            mul = arr[i]
        else:
            mul = mul * arr[i]
        right[i-1] = mul
        
    for i in range(len(arr)):
        print (left[i]*right[i])


if __name__ == "__main__":
    arr = [10, 3, 5, 6, 2]
    solve(arr)