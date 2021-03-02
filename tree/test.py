class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root,node,k):
    if not root:
        return -1
    if root == node:
        return 0
    l = solve(root.left,node,k)
    if l != -1:
        if 1+l == k:
            print (root.val)
        else:
            solve(root.right,node,k-l-2)
        return 1 + l
    r = solve(root.right,node,k)
    if r != -1:
        if 1+r == k:
            print (root.val)
        else:
            solve(root.left,node,k-r-2)
        return 1 + r
    return -1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solve(root,root.left,2)