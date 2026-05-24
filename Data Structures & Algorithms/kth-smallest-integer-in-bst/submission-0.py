# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val = [0]
        count = [0]
        self.dfs(root, k, val, count)
        return val[0]
    
    def dfs(self, root: Optional[TreeNode], k: int, val: list, count: list):
        if root is None:
            return
        
        if count[0] > k:
            return
        
        self.dfs(root.left, k, val, count)

        count[0] = count[0] + 1
        print(count, val)
        if count[0] == k:
            val[0] = root.val
            return
        
        self.dfs(root.right, k, val, count)

        