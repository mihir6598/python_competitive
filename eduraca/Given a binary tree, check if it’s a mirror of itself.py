class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def solve(root1,root2):
    if not root1 and not root2:
        return True
    if root1 and root2 and root1.val == root2.val and solve(root1.left,root2.right) and solve(root1.right,root2.left):
        return True
    return False

if __name__ =="__main__" :
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    print (solve(root,root)) 