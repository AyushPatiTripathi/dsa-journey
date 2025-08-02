class Solution:
    def isPalindrome(self, x: int) -> bool:
        num =  x 
        reverse = 0 
        while num > 0 :
            digit = num % 10 
            reverse = (reverse * 10) + digit 
            num = num // 10 
        if reverse == x :
            return True 
        else :
            return False
        
