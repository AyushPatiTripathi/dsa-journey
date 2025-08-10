class Solution:
    def sortColors(self, nums: List[int]) -> None:
        pointer = 0
        while pointer < len(nums) - 1:
            if nums[pointer] > nums[pointer + 1]:
                nums[pointer], nums[pointer + 1] = nums[pointer + 1], nums[pointer]
                pointer = 0  # restart from beginning after a swap
            else:
                pointer += 1

        
