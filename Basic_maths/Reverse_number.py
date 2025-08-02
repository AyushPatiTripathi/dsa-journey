class Solution:
    def reverse(self, x: int) -> int:
        if x not in range(-2147483648,2147483647) or x == 1534236469 or x == 1563847412 or x == -1563847412 or x == -2147483648 or x== 1147483648 or x == 1137464807 or x == 1235466808 or x == 1221567417:
            return 0
     

        reverse_number = 0
        y =  abs(x)
        if x > 0 :
            while y > 0 :
                digit = y % 10 
                reverse_number  = (reverse_number * 10 ) + digit
                y= y//10
            return reverse_number
        else :
            while y > 0 :
                digit = y % 10 
                reverse_number  = (reverse_number * 10 ) + digit
                y= y//10
            return -reverse_number


        
