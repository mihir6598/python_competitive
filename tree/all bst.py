class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    if not root:
        return
    print (root.val,end=" ")
    preorder(root.left)
    preorder(root.right)


def solve(arr):
    if len(arr) == 1:
        return [TreeNode(arr[0])]
    temp = []
    for i in range(len(arr)):
        
        left = arr[:i]
        right = arr[i+1:]
        print (arr[i],left,right)
        if left:
            l = solve(left)
        else:
            l = [None]
        if right:
            r = solve(right)
        else:
            r = [None]
        for k in l:
            for l in r:
                root = TreeNode(arr[i])
                root.left = k
                root.right = l 
                temp.append(root)
    return temp
        



if __name__ == "__main__":
    arr = [1,2,3]
    main_length = len(arr)
    main_root = None
    for i in solve(arr):
        print ("")
        preorder(i)