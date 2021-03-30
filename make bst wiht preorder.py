class Solution:
    def bstFromPreorder(self, arr: List[int]) -> TreeNode:
        def solve(root,arr):
            if not arr:
                return 
            count = 0
            for i in arr:
                if i < root.val:
                    count = count + 1
                else:
                    break
            left = arr[:count]
            right = arr[count:]
            if left:
                root.left = TreeNode(left.pop(0))
                solve(root.left,left)
            if right:
                root.right = TreeNode(right.pop(0))
                solve(root.right,right)
        final = TreeNode(arr[0])
        solve(final,arr[1:])
        return final

