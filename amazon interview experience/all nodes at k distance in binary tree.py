class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def print_down(root,k):
    if not root:
        return
    if k == 0:
        print (root.val)
        return 
    print_down(root.left,k-1)
    print_down(root.right,k-1)
        
def solve(root,k,node):
    if not root:
        return -1
    if root == node:
        print_down(root,k)
        return 0
    l = solve(root.left,k,node)
    if l != -1:
        
        if l + 1 == k:
            print (root.val)
        else:
            print_down(root.right,k-l-2)
        return l + 1
    r = solve(root.right,k,node)
    if r != -1:
        if r+1 == k:
            print (root.val)
        else:
            print_down(root.left,k-r-2)
        
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    solve(root,1,root.left)