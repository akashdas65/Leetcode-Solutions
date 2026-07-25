# LeetCode 3536- Maximum Product of Two Digits
# Category: Math

# Approach:
# Traverse all digits of the given number using modulo (%) and integer
# division (//). Maintain the largest and second largest digits seen so far.
# - If the current digit is greater than or equal to the largest digit,
#   update both the largest and second largest.
# - Otherwise, if it is greater than the second largest digit,
#   update the second largest.
# After processing all digits, return the product of the two largest digits.
#
# Time Complexity: O(d)
# where d is the number of digits in n.
#
# Space Complexity: O(1)

class Solution:
    def maxProduct(self, n: int) -> int:
        first = 0
        second = 0

        while n > 0:
            digit = n % 10

            if digit >= first:
                second = first
                first = digit
            elif digit > second:
                second = digit

            n //= 10

        return first * second
