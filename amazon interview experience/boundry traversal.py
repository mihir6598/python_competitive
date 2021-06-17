class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def print_leaves(root):
    if not root:
        return 
    if not root.left and not root.right:
        print (root.val)
        return 
    print_leaves(root.left)
    print_leaves(root.right)
        
def print_left(root):
    if not root:
        return
    if root.left:
        print (root.val)
        print_left(root.left)
    elif root.right:
        print (root.val)
        print_left(root.right)
        
def print_right(root):
    if not root:
        return  
    if root.right:
        print_right(root.right)
        print (root.val)
        
    elif root.left:
        print_right(root.left)
        print (root.val)

        
def solve(root):
    if not root:
        return
    print (root.val)
    print_left(root.left)
    print_leaves(root.left)
    print_leaves(root.right)
    print_right(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    solve(root)