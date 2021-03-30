class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    global sum
    if not root:
        return 0
    solve(root.right)
    sum = sum + root.val
    root.val = sum - root.val
    solve(root.left)

def solve2(root):
    solve(root)
     
def p(root):
    if not root:
        return 
    p(root.right)
    print (root.val)
    p(root.left)


if __name__ == '__main__':
    root = TreeNode(11)
    root.left = TreeNode(2)
    root.right = TreeNode(29)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(40)
    root.right.left = TreeNode(15)
    root.right.right.left = TreeNode(35)
    sum = 0
    solve(root)
    p(root)