# LeetCode 7 - Reverse Integer
# Optimal Solution
# Uses arithmetic operations instead of string conversion
# Checks for 32-bit integer overflow
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        rev *= sign

        if rev < -(2**31) or rev > (2**31 - 1):
            return 0

        return rev
