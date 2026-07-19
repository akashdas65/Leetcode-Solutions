# LeetCode 125 - Valid Palindrome
#
# Category: String, Two Pointers
#
# Approach:
# Use two pointers, one starting from the beginning and the other
# from the end of the string. Skip all non-alphanumeric characters
# and compare the remaining characters in lowercase. If all pairs
# match, the string is a valid palindrome.
#
# Time Complexity: O(n)
#
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:

            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True