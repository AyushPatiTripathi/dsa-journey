class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for _ in strs :
            while  not _.startswith(prefix) :
                prefix = prefix[:-1]
                if prefix == "" :
                    return ""
    
        return prefix 
