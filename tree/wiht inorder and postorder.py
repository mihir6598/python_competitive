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

def makeTree(start,end):
    print (start,end)
    if start == end:
        return TreeNode(postorder.pop())
    if start >end:
        return None
    rootVal = postorder.pop()
    print (rootVal)
    root = TreeNode(rootVal)
    root.right = makeTree(inorderMap[rootVal]+1,end)
    root.left = makeTree(start,inorderMap[rootVal]-1)
    return root

if __name__ == "__main__":
    inorder = [3,2,1]
    postorder = [3,2,1]
    inorderMap = {}
    for i in range(len(inorder)):
        inorderMap[inorder[i]] = i
    root = makeTree(0,len(postorder)-1)
    printTree(root)