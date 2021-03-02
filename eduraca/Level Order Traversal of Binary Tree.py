class TreeNode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def solve(root):
    q = [root]
    while q:
        root = q.pop(0)
        print (root.data)
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    # root.left.left = TreeNode(7)
    root.left.right = TreeNode(5)
    solve(root)
