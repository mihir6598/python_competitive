def solve(arr,k):
    n = len(arr)
    stack = []
    for i in range(k):
        if not stack:
            stack.append(i)
        else:
            while stack and arr[stack[-1]]<arr[i]:
                stack.pop()
            stack.append(i)
    print (stack)
    print (arr[stack[0]])
    for i in range(k,n):
        if stack[0]<i-k+1:
            stack.pop()
        while stack and arr[stack[-1]]<arr[i]:
            stack.pop()
        stack.append(i)
        print (arr[stack[0]])
    


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    solve(arr,3)