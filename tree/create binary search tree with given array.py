def inorder(arr,n,inorder_arr):
    if n>=len(arr):
        return
    inorder(arr,n*2+1,inorder_arr)
    inorder_arr.append(arr[n])
    inorder(arr,n*2+2,inorder_arr)

def solve(arr):
    inorder_arr = []
    inorder(arr,0,inorder_arr)
    arr_sorted = arr.copy()
    arr_sorted.sort()
    index = {}
    for i in range(len(inorder_arr)):
        index[inorder_arr[i]] = i
    ans = 0
    for i in range(len(inorder_arr)):
        if inorder_arr[i] != arr_sorted[i]:
            ans += 1
            temp = inorder_arr[i]
            inorder_arr[i],inorder_arr[index[arr_sorted[i]]] = inorder_arr[index[arr_sorted[i]]],inorder_arr[i]
            index[arr_sorted[i]],index[temp] = index[temp],index[arr_sorted[i]]
             
    print (ans)
    print (inorder_arr)

if __name__ == "__main__":
    arr = [ 5, 6, 7, 8, 9, 10, 11 ]
    solve(arr)