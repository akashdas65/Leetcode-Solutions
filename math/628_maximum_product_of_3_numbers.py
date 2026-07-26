# LeetCode 628 - Maximum Product of Three Numbers
# Category: Array, Math

# Approach:
# Traverse the array once while maintaining:
# - The three largest numbers (first, second, third).
# - The two smallest numbers (small1, small2).
#
# The maximum product can be either:
# 1. The product of the three largest numbers.
# 2. The product of the two smallest (most negative) numbers
#    and the largest number.
#
# Return the maximum of these two products.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first = second = third = float("-inf")
        small1 = small2 = float("inf")

        for num in nums:

            # Update the three largest numbers
            if num >= first:
                third = second
                second = first
                first = num
            elif num >= second:
                third = second
                second = num
            elif num > third:
                third = num

            # Update the two smallest numbers
            if num <= small1:
                small2 = small1
                small1 = num
            elif num < small2:
                small2 = num

        # Product of three largest numbers
        product1 = first * second * third

        # Product of two smallest numbers and the largest number
        product2 = small1 * small2 * first

        # Return the maximum product
        return max(product1, product2)