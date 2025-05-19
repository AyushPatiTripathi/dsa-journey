class Solution(object):
    def romanToInt(self, s):
        special = { 
            "IV" : 4, "IX" : 9 , "XL":40 ,
            "XC" : 90 , "CD" : 400, "CM" :900
        }

        values = {
            "I" :1 , "V": 5, "X": 10 ,
            "L" :50 , "C": 100 , "D" : 500 , "M":1000

        }
        i = 0
        total = 0
        while i < len(s):
            if i+ 1 < len(s) and s[i:i+2] in special :
                total  += special[s[i:i+2]]
                i += 2 
            else :
                total  += values[s[i]]
                i += 1 
        return total
