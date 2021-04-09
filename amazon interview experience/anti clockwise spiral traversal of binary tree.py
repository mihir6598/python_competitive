class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def levelprint(root):
    final = []
    q = [(root,0)]
    maxlevel = -1
    while(q):
        root,level = q.pop(0)
        if level>maxlevel:
            final.append([root.val])
            maxlevel = level
        else:
            final[level].append(root.val)
        if root.left:
            q.append((root.left,level+1))
        if root.right:
            q.append((root.right,level+1))
    print (final)
    for i in range(len(final)//2):
        [print (i) for i in final[i][::-1]]
        [print (i) for i in final[len(final)-i-1]]
    if len(final)%2 == 1:
        [print (i) for i in  (final[len(final)//2][::-1])]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(6)
    levelprint(root)