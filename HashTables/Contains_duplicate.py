class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_nums = set(nums)
        a = len(new_nums)
        b = len(nums)
        if a != b:
            return True
        else :
            return False

