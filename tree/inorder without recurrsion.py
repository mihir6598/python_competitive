class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def printTree(root):
    if not root:
        return
    printTree(root.left)
    print (root.val)
    printTree(root.right)

def solve(root):
    stack = []
    current = root
    
    while True:
        if current:
            stack.append(current)
            current = current.left
        else:
            if stack:
                temp = stack.pop()
                print (temp.val)
                current = temp.right
            else:
                break
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    printTree(root)
    solve(root)
