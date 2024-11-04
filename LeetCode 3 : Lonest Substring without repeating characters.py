class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0 
        max_length = 0 
        set_char = set()

        for right in range(len(s)):
            while s[right] in set_char: 
                set_char.remove(s[left])
                left = left + 1

            set_char.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
