class Solution:
    def check(self, nums: List[int]) -> bool:
        
        count = 0 
        for i in range (0,len(nums)-1):
            if nums[i] > nums[i+1] :
                count +=  1 
               
            
        if nums[-1] > nums[0] :
            count = count +  1
        if count >= 2 :
            return False
        else :
            return True 
        
