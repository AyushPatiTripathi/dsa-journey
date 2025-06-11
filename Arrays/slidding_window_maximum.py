from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()  # stores indices, not values
        ans = []

        for i in range(len(nums)):
            # Remove indices of elements not in the current window
            while window and window[0] <= i - k:
                window.popleft()

            # Remove elements smaller than the current one from the back
            while window and nums[window[-1]] < nums[i]:
                window.pop()

            window.append(i)

            # Append max (front of deque) once we reach size k
            if i >= k - 1:
                ans.append(nums[window[0]])

        return ans

       


