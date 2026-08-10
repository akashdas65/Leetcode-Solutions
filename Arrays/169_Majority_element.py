# LeetCode 169 - Majority Element
# Pattern: Boyer-Moore Voting Algorithm
# Difficulty: Easy
#
# Question:
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than n / 2 times.
# It is guaranteed that a majority element always exists.
#
# Example:
# Input:  nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Approach:
# 1. Maintain a candidate and its count.
# 2. If count becomes 0, select the current number as candidate.
# 3. If the current number equals the candidate, increase count.
# 4. Otherwise, decrease count.
# 5. The final candidate is the majority element.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        # Initialize the candidate
        candidate = 0

        # Initialize the voting count
        count = 0

        # Traverse through every number in the array
        for num in nums:

            # If count becomes 0,
            # select the current number as the candidate
            if count == 0:
                candidate = num

            # If the current number matches the candidate,
            # increase the count
            if num == candidate:
                count += 1

            # If the current number is different from the candidate,
            # decrease the count
            else:
                count -= 1

        # Return the final majority element
        return candidate