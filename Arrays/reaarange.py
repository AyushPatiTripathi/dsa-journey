class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        pos_list = []
        neg_list = []
        for num in nums :
            if num > 0 :
                pos_list.append(num) 
            else :
                neg_list.append(num)
        for i in range(0,len(nums)) :
            if i % 2 == 0 :
                a =  pos_list.pop(0)
                ans.append(a)
            else :
                a = neg_list.pop(0)
                ans.append(a)
        return ans


        
