def solve(arr):
    sum = {}
    s = 0
    ans = []
    for i in range(len(arr)):
        s = s + arr[i]
        if s == 0:
            ans.append((0,i))
        
        if s in sum:
            for j in sum[s]:
                ans.append((j+1,i))
            sum[s].append(i)
        else:
            sum[s] = [i]
    print (ans)

if __name__ == "__main__":
    arr = [1,2,-3,1,-4,6]
    solve(arr)