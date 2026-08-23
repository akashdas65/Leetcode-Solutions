# LeetCode 1927 - Sum Game
# Pattern: Greedy
# Difficulty: Medium
#
# Question:
# Alice and Bob take turns replacing '?' with digits.
# Alice wins if the final number's left-half digit sum
# is different from the right-half digit sum.
#
# Approach:
# 1. Calculate the sum of known digits in both halves.
# 2. Count '?' in both halves.
# 3. If total '?' is odd, Alice always wins.
# 4. Otherwise, calculate the maximum possible compensation.
# 5. If the existing difference can be balanced exactly, Bob wins.
# 6. Otherwise, Alice wins.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def sumGame(self, num: str) -> bool:

        # Find the middle of the string
        half = len(num) // 2

        # Store the sum of known digits in the left half
        left_sum = 0

        # Store the sum of known digits in the right half
        right_sum = 0

        # Count '?' in the left half
        left_q = 0

        # Count '?' in the right half
        right_q = 0

        # Traverse the left half
        for i in range(half):

            # If current character is '?'
            if num[i] == '?':
                left_q += 1

            # Otherwise, add the digit to left sum
            else:
                left_sum += int(num[i])

        # Traverse the right half
        for i in range(half, len(num)):

            # If current character is '?'
            if num[i] == '?':
                right_q += 1

            # Otherwise, add the digit to right sum
            else:
                right_sum += int(num[i])

        # If the total number of '?' is odd,
        # Alice can always force a difference
        if (left_q + right_q) % 2 == 1:
            return True

        # Calculate the difference between the known sums
        difference = left_sum - right_sum

        # Calculate the difference in the number of '?' characters
        question_difference = right_q - left_q

        # Bob wins only when the difference can be balanced exactly
        if difference == question_difference * 4.5:
            return False

        # Otherwise Alice wins
        return True