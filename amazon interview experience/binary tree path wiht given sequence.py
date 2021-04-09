class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def solve2(root,i):
    global arr
    if not root:
        return False
    # print (root.val,i)
    
    if root.val == arr[i]:
        if i == len(arr)-1:
            return True
        l = solve2(root.left,i+1)
        r = solve2(root.right,i+1)
        return l or r
    return False
    

def solve(root):
    global arr,i
    if i == len(arr):
        print ("found")
        return 1
    if not root:
        return 0
    if root.val == arr[i]:
        temp = solve2(root,i)
        if temp:
            print ("found")
            return 1
        i = i+1
        return 1
    l = solve(root.left)
    if l:
        if root.val == arr[i]:
            temp = solve2(root,i)
            if temp:
                print ("found")
                return 1
            i = i+1
            return 1
        else:
            return 0

    r = solve(root.right)
    if r:
        if root.val == arr[i]:
            temp = solve2(root,i)
            if temp:
                print ("found")
                return 1
            i = i+1
            return 1
        else:
            return 0
    return 0
    

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    arr = [6,7,3]
    i = 0
    print (solve(root))
    # print (solve2(root.right,0))