class Solution(object):
    
    def maxSubArray( self ,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math 
        max_sum =-99999999999999
        curr_sum =0
        for num in nums :
            curr_sum =max(num,curr_sum +num)
            max_sum = max(max_sum ,curr_sum)

            
            
        return max_sum
   
