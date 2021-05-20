class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

def solve(root):
    q1 = [root]
    q2 = []

    while (q1):
        for i in range(len(q1)):
            temp = q1.pop()
            print (temp.val)
            
            if temp.left:
                q2.append(temp.left)
            if temp.right:
                q2.append(temp.right)
        for i in range(len(q2)):
            temp = q2.pop()
            print (temp.val)
            if temp.right:
                q1.append(temp.right)
            if temp.left:
                q1.append(temp.left)
            
            
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    solve(root)