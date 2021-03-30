# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def solve(root):
            nonlocal m_ans
            if not root:
                return 0
            l = solve(root.left)
            r = solve(root.right)
            left = 0
            right = 0
            
            if root.left and root.left.val == root.val:
                left = l + 1
            if root.right and root.right.val == root.val:
                right = 1 + r
            if left and right:
                m_ans = max(m_ans,l+r+2)
            m = max(left,right)
            m_ans = max(m,m_ans)
            return m
        m_ans = 0
        solve(root)
        return m_ans
                
https://leetcode.com/problems/longest-univalue-path/