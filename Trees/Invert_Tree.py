# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
       
        queue =deque([root])

        while queue :
            node = queue.popleft()
            if not node:
                continue 
            node.left , node.right = node.right ,node.left

            if node.left:
                queue.append(node.left)
            if node.right :
                queue.append(node.right)
        return root 

