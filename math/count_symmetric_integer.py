# LeetCode 2843. Count Symmetric Integers
# Difficulty: Easy
# Language: Python 3
#
# Approach:
# - Iterate through every number from low to high.
# - Convert the number to a string.
# - Ignore numbers with an odd number of digits.
# - Split the string into two equal halves.
# - Calculate the sum of digits in each half.
# - If both sums are equal, increment the count.
#
# Time Complexity: O((high - low + 1) × d)
# d = Number of digits in the number
#
# Space Complexity: O(1)

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high + 1):
            s = str(num)

            # Skip numbers with an odd number of digits
            if len(s) % 2 != 0:
                continue

            mid = len(s) // 2

            # Sum of first half digits
            left_sum = sum(int(digit) for digit in s[:mid])

            # Sum of second half digits
            right_sum = sum(int(digit) for digit in s[mid:])

            # Check if both halves have the same digit sum
            if left_sum == right_sum:
                count += 1

        return count
