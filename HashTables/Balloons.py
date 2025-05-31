class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < 5:
            return 0 
            
        char_count = {"b":0, "a":0, "l":0, "o":0, "n":0}
        count = 0
        
        # Count relevant characters
        for char in text:
            if char in char_count:
                char_count[char] += 1
        
        # Keep making balloons until we can't anymore
        while True:
            # Check if we have enough letters for one more balloon
            if (char_count["b"] >= 1 and 
                char_count["a"] >= 1 and 
                char_count["l"] >= 2 and 
                char_count["o"] >= 2 and 
                char_count["n"] >= 1):
                
                # Subtract one balloon's worth of letters
                char_count["b"] -= 1
                char_count["a"] -= 1
                char_count["l"] -= 2  # balloon has two 'l's
                char_count["o"] -= 2  # balloon has two 'o's
                char_count["n"] -= 1
                
                count += 1
            else:
                break
                
        return count
