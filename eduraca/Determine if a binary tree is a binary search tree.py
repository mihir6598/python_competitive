class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def solve(root,min,max):
    if not root:
        return True
    if root.val>max or root.val<min:
        return False
    return (solve(root.left,min,root.val) and solve(root.right,root.val,max))



if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(11)
    print (solve(root,-float("inf"),float("inf")))
