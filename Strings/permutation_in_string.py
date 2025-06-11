class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge condition
        if not s2 or len(s2) < len(s1):
            return False

        s1_sorted = ''.join(sorted(s1))
        k = len(s1)

        for i in range(len(s2) - k + 1):
            window = s2[i:i+k]
            if ''.join(sorted(window)) == s1_sorted:
                return True

        return False


        
            
        
