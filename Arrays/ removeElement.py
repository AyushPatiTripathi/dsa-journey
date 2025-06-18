class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # Slow pointer (write index)
        for j in range(len(nums)):  # Fast pointer (read index)
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
        
