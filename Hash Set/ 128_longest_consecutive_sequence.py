# LeetCode 128 - Longest Consecutive Sequence
# Pattern: Hash Set
# Difficulty: Medium
#
# Approach:
# 1. Store all numbers in a set for O(1) average lookup.
# 2. Check if the current number is the start of a sequence.
# 3. If num - 1 is not present, start counting consecutive numbers.
# 4. Keep updating the maximum sequence length.
#
# Time Complexity: O(n) average
# Space Complexity: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Convert the list into a set for fast lookup
        num_set = set(nums)

        # Store the longest consecutive sequence length
        longest = 0

        # Check every unique number
        for num in num_set:

            # Start only if num is the beginning of a sequence
            if num - 1 not in num_set:

                # Start the sequence with length 1
                length = 1

                # Keep checking the next consecutive number
                while num + length in num_set:
                    length += 1

                # Update the longest sequence length
                longest = max(longest, length)

        # Return the longest consecutive sequence
        return longest