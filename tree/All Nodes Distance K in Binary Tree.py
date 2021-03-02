class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def save_depth(root,depth):
            if not root:
                return
            if depth == 0:
                final.append(root.val)
            save_depth(root.left,depth-1)
            save_depth(root.right,depth-1)
        
        def solve(root,node,k):
            
            if not root:
                return -1
            if root == node:
                save_depth(root,k)
                return 0
            
            l = solve(root.left,node,k)
            if l != -1:
                if 1 + l == k:
                    final.append(root.val)
                else:
                    save_depth(root.right,k-l-2)
                return 1 + l
            
            r = solve(root.right,node,k)
            if r != -1:
                if 1 + r == k:
                    final.append(root.val)
                else:
                    save_depth(root.left,k-r-2)
                return 1 + r
            return -1
        final = []
        solve(root,target,K)
        return final


https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/