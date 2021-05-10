class treeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def printtree(root):
    if not root:
        return
    
    printtree(root.left)
    print (root.val)
    printtree(root.right)

def solve(arr):
    print (arr)
    if not arr:
        return [None]
    if len(arr) == 1:
        return [treeNode(arr[0])]
    temp = []
    for i in range(len(arr)):
        left = arr[:i]
        right = arr[i+1:]
    
        for j in solve(left):
            for k in solve(right):
                root = treeNode(arr[i])
                root.left = j
                root.right = k
                temp.append(root)
    print (temp)
    return temp
    


if __name__ == "__main__":
    arr = [3,2,5]
    for i in solve(arr):
        printtree(i)