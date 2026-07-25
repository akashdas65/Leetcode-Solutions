# LeetCode 9 - Palindrome Number
# Category: Math

# Approach:
# Store the original number in a variable.
# Reverse the entire number by extracting its last digit repeatedly.
# Compare the reversed number with the original number.
# If they are equal, the number is a palindrome; otherwise, it is not.
#
# Note:
# Negative numbers are never palindromes because of the '-' sign.

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers cannot be palindromes
        if x < 0:
            return False

        original = x
        reverse = 0

        # Reverse the number
        while x > 0:
            reverse = reverse * 10 + (x % 10)
            x //= 10

        # Compare reversed number with original
        return reverse == original
