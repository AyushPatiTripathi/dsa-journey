# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def pre_order(node) :
            if not node :
                return
            ans.append(node.val)
            pre_order(node.left)
            pre_order(node.right)
        pre_order(root)    
        return ans        
