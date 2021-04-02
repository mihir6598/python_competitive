def change(i,j,n,m):
    if i < 0 or i >=n or j <0 or j>=m or arr[i][j] == "X" or arr[i][j] == "O":
        return
    
    arr[i][j] = "O"
    change(i+1,j,n,m)
    change(i-1,j,n,m)
    change(i,j+1,n,m)
    change(i+1,j-1,n,m)
    

def solve(arr):
    n = len(arr)
    m = len(arr[0])

    for i in range(n):
        for j in range(m):
            if arr[i][j] == "O":
                arr[i][j] = "-"
    
    for i in range(n):
        if arr[i][0] == "-":
            change(i,0,n,m)
    print (arr)
    for i in range(n):
        if arr[i][m-1] == "-":
            change(i,m-1,n,m)
    
    for i in range(m):
        if arr[0][i] == "-":
            change(0,i,n,m)

    for i in range(m):
        if arr[n-1][i] == "-":
            change(n-1,i,n,m)
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "-":
                arr[i][j] = "X"
    print (arr)

if __name__ == "__main__":
    arr = [['X', 'O', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X', 'O', 'X'],
        ['X', 'X', 'X', 'O', 'O', 'X'],
        ['O', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'O', 'X', 'O'],
        ['O', 'O', 'X', 'O', 'O', 'O']]

    solve(arr)