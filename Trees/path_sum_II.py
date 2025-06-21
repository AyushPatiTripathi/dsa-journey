# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def has_sum(root,cur_sum,path =None , ans =None) :
            if path == None :
                path = []
            if ans == None :
                ans = []
            if not root :
                return 
            cur_sum += root.val
            path.append(root.val)

            if not root.left and  not root.right :
                if cur_sum == targetSum :
                    ans.append(path.copy())
            else :
                has_sum(root.left ,cur_sum ,path ,ans)
                has_sum(root.right ,cur_sum ,path ,ans)
            path.pop()

        result = [] 
        has_sum(root , 0 , [], result)
        return result   
        
        
