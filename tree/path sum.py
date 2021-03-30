

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root,v,k):
    global final
    if v == k and not root.left and not root.right:
        print (final)
        return True
    l = False
    if root.left:
        final.append(root.left.val)
        l = solve(root.left,v+root.left.val,k)
        final.pop()
    if root.right:
        final.append(root.right.val)
        l = solve(root.right,v+root.right.val,k)
        final.pop()
    return l
def test(root):
    global final
    if not root:
        print (final)
        return
    final.append(root.val)
    test(root.left)
    test(root.right)
    final.pop()

root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(10)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.right = TreeNode(2)
final = []
# print (solve(root,root.val,32))
test(root)
# print (dfs(root))