class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N =len(nums) 
        l =0 
        r =  N - 1 
        if target > nums[r] :
            return r +1
        elif target <nums[l] :
            return l       
        

        while l <= r :
            m = l +((r-l)// 2 )

            if nums[m] == target :
                return m
            elif target < nums[m] :
                r = m -1 
            else :
                l = m + 1  
        return l
