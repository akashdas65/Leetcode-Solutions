# LeetCode 66 - Plus One

# Approach:
# Traverse the array from right to left because addition starts from the last digit.
# If the current digit is less than 9, increment it by 1 and return the array.
# If the digit is 9, set it to 0 and continue carrying 1 to the previous digit.
# If all digits are 9, create a new array with a leading 1 followed by all zeros.


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits

# Time Complexity: O(n)
# Space Complexity: O(1)