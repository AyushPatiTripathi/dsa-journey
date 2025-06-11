class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Step 1: Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Step 2: Compare lowercase letters
            if s[left].lower() != s[right].lower():
                return False

            # Step 3: Move pointers inward
            left += 1
            right -= 1

        return True

