class GFG:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def check(root,parent):
    print ("in")
    if not root:
        return True
    if root.val>parent:
        return False
   
    return (check(root.left,root.val) and check(root.right,root.val))




root = GFG(5)
root.left = GFG(2)
root.right = GFG(3)
root.left.left = GFG(5)
print (check(root,float("inf")))