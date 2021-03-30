class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def main_left(root):
    if not root:
        return
    print (root.val)
    main_left(root.left)
    leaf(root.right)

def main_right(root):
    if not root:
        return
    leaf(root.left)
    main_left(root.right)
    print (root.val)    

def leaf(root):
    if not root:
        return
    if not root.left and not root.right:
        print (root.val)
    leaf(root.left)
    leaf(root.right)

def dfs(tree):
    return dfs(tree.left)+dfs(tree.right)+[tree.val] if tree else []

root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(4)
root.left.right = TreeNode(12)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)
root.right.right = TreeNode(25)
# print (dfs(root))
print (root.val)
main_left(root.left)
main_right(root.right)
# solve(root,root.left,2)