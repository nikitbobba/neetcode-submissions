import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = queue.Queue()
        if root is None:
            return []
        
        res = []
        prevLevel = None
        q.put((root, 1))
        tmp = []
        while not q.empty():
            curr, level = q.get()

            if prevLevel == level:
                res[-1].append(curr.val)
            else:
                # its a new level
                #
                res.append([curr.val])
            
            prevLevel = level
            if curr.left is not None:
                q.put((curr.left, level+1))
            
            if curr.right is not None:
                q.put((curr.right, level+1))

        return res

            
        