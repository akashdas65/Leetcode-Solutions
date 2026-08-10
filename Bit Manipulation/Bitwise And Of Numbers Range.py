# LeetCode 201 - Bitwise AND of Numbers Range
# Pattern: Bit Manipulation
# Difficulty: Medium
#
# Question:
# Given two integers left and right that represent the range [left, right],
# return the bitwise AND of all numbers in this range, inclusive.
#
# Example:
# Input:  left = 5, right = 7
# Output: 4
#
# Explanation:
# 5 = 101
# 6 = 110
# 7 = 111
# ------------
# AND = 100 = 4
#
# Approach:
# 1. Find the common binary prefix of left and right.
# 2. Right shift both numbers until they become equal.
# 3. Count how many right shifts were performed.
# 4. Left shift the common prefix back to its original position.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        # Store the number of right shifts performed
        shift = 0

        # Keep removing the different rightmost bits
        # until left and right have the same binary prefix
        while left != right:

            # Right shift left by one bit
            left >>= 1

            # Right shift right by one bit
            right >>= 1

            # Count the number of shifts
            shift += 1

        # Shift the common prefix back to its original position
        return left << shift