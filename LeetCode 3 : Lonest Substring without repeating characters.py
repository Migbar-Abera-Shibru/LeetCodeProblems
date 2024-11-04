# Time complexity : O(n)
# Space complexity: O(min(m,n) m is the size of the character

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0 # This is a pointer that marks the start of the current substring. It will slide to the right whenever we encounter a duplicate character
        max_length = 0 # This keeps track of the maximum length of a substring without repeating characters
        set_char = set() # A set that holds characters in the current substirng which allosws us to check for duplicates quickly

        for right in range(len(s)): 
            while s[right] in set_char: # we check if each charactres is already in set_char. if it is already there then remove s[left] from set_char and move left one position to the right.
                set_char.remove(s[left])
                left = left + 1

            set_char.add(s[right]) # if not in the set_char then add it and calculate the max_length by comparing it to the current maximum length and return it.
            max_length = max(max_length, right - left + 1)
        
        return max_length
