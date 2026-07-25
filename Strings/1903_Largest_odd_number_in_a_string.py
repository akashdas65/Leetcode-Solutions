# LeetCode 1903 - Largest Odd Number in String
# Category: String, Greedy

# Approach:
# Traverse the string from right to left.
# Find the first odd digit (1, 3, 5, 7, or 9).
# Since removing digits from the end produces the largest possible prefix,
# return the substring from the beginning up to and including that odd digit.
# If no odd digit exists, return an empty string.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def largestOddNumber(self, num: str) -> str:

        # Traverse from the last digit to the first
        for i in range(len(num) - 1, -1, -1):

            # Check if the current digit is odd
            if int(num[i]) % 2 == 1:

                # Return the largest odd prefix
                return num[:i + 1]

        # No odd digit found
        return ""
