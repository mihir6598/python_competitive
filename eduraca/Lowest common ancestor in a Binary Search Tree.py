class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def solve_binary(root,node1,node2):
    if not root:
        return
    if root.val>node1.val and root.val>node2.val:
        print ("in")
        return solve_binary(root.left,node1,node2)
    
    if root.val<node1.val and root.val<node2.val:
        return solve_binary(root.right,node1,node2)
    return root

def solve(root,node1,node2):
    global ans
    if not root:
        return 
    l = solve(root.left,node1,node2)
    r = solve(root.right,node1,node2)
    if l and r:
        ans = root
    if root == node1 or root == node2:
        if l or r:
            ans = root
        return True
    if l or r:
        return True
    return False
    


if __name__ =="__main__" :
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    p = []
    final = []
    ans = None
    print (solve(root,root.left.right,root.right))
    print (ans.val)
    # print (solve_binary(root,root.left.left,root.right.right).val)
    