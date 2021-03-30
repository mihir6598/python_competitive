def legal(p):
    global n,m
    if p[0]>=0 and p[0]<n and p[1]>=0 and p[1]<m :
        return True
    return False 
def legal2(p):
    global n,m
    if p[0]>=0 and p[0]<n and p[1]>=0 and p[1]<m :
        return True
    return False 


def correct(start,end):
    if (start[0]+1,start[1]) == end or (start[0],start[1]+1) == end or start == end:
        return True
    return False
def solve2(arr,start,end):
    global ans
    global count
    count = count + 1
    if not legal(start) or not legal2(end):
        return
    if arr[start[0]][start[1]] != arr[end[0]][end[1]]:
        return
    if correct(start,end):
        ans = ans + 1
        return
    
    
    solve2(arr,(start[0]+1,start[0]),(end[0]-1,end[1]))
    solve2(arr,(start[0],start[1]+1),(end[0]-1,end[1]))
    solve2(arr,(start[0]+1,start[1]),(end[0],end[1]-1))
    solve2(arr,(start[0],start[1]+1),(end[0],end[1]-1))

def solve(arr):
    n = len(arr)
    m = len(arr[0])
    start = (0,0)
    end = (n-1,m-1)
    solve2(arr,start,end)
    print (ans)
    print (count)


if __name__ == "__main__":
    arr = ["aa", "aa"]
    count = 0
    ans = 0
    n = len(arr)
    m = len(arr[0])
    solve(arr)