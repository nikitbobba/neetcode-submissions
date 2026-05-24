# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p1 = p
        p2 = q

        return self.dfs(p1, p2)

    def dfs(self, p1, p2):
        if p1 is None and p2 is not None:
            return False
        if p2 is None and p1 is not None:
            return False
        
        if p1 is None and p2 is None:
            return True
        
        return (p1.val == p2.val) and self.dfs(p1.left, p2.left) and self.dfs(p1.right, p2.right)

        