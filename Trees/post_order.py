# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def order(node) :
            if not node :
                return
            order(node.left)
            order(node.right)
            ans.append(node.val)
        order(root)

        return ans
            
