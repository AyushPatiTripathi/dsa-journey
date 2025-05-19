class Solution(object):
    def findClosestNumber(self, nums):
        self.nums = nums
        distance= 0
        least_distance = float('inf')
        closest_num = 0
        for num in self.nums :
            distance = abs(num - 0)
            if distance < least_distance :
                least_distance = distance 
                closest_num = num
            elif distance == least_distance :
                if num > closest_num:
                    closest_num = num
        return  closest_num
                
