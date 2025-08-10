class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pointer =  0 
        store =set(nums)
        num = list(store)

        
        
       
        while pointer < len(num) :
            target_item = num[pointer]
            count = 0
            for  i in nums :
                if i == target_item :
                    count = count + 1 
            if  count  > len(nums)/2 :
                return num[pointer]
            pointer += 1 
              

