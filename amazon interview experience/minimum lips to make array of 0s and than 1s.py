def solve(arr):
    total_z = 0
    total_o = 0
    for i in arr:
        if i == 0:
            total_z += 1
        else:
            total_o += 1
    ans = float("inf")   
    z = 0
    o = 0 
    for i in arr:
        if i == 0:
            z += 1
        else:
            o += 1
        ans = min(ans,o+total_z-z)
    return ans

if __name__ == "__main__":
    arr = [1,0,0,1,0,1]
    print (solve(arr))