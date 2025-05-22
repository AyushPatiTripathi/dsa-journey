class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0  # Empty array edge case

        write_index = 0  # Initialize write pointer

    # Start reading from second element
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[write_index]:
                write_index += 1  # Move write pointer forward
                nums[write_index] = nums[read_index]  # Overwrite with new unique element

    # Number of unique elements is write_index + 1
        return write_index + 1

