class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       # edgew conditions 
       if len(ransomNote) > len(magazine) :
        return False 
       if len(ransomNote) == 0 :
        return True 
       char_count= {}

       for char in magazine :
        if char in char_count :
            char_count[char] += 1 
        else :
            char_count[char]= 1
       for char in ransomNote :
        if char not in  char_count or char_count[char] <=0 :
            return False
        char_count[char] -= 1
       return True 

