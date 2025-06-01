class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # Opening bracket
                stack.append(char)
            elif stack and mapping[char] == stack[-1]:  # Matching closing bracket
                stack.pop()
            else:
                return False  # Mismatch or extra closing bracket
        
        return not stack  # True if stack is empty
