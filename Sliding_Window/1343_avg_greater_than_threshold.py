# LeetCode 1343 - Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Pattern: Sliding Window
# Difficulty: Medium
#
# Question:
# Given an array of integers arr and two integers k and threshold,
# return the number of sub-arrays of size k whose average is greater
# than or equal to threshold.
#
# Example:
# Input:  arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
#
# Explanation:
# The sub-arrays with an average greater than or equal to 4 are:
# [2,5,5], [5,5,5], [5,5,8]
#
# Approach:
# 1. Calculate the sum of the first k elements.
# 2. Instead of calculating the average, compare the sum with k * threshold.
# 3. Slide the window one position at a time.
# 4. Add the new element entering the window.
# 5. Remove the element leaving the window.
# 6. If the window sum is at least k * threshold, increase the answer.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:

        # Calculate the minimum sum required for a valid sub-array
        target = k * threshold

        # Calculate the sum of the first window of size k
        window_sum = sum(arr[:k])

        # Store the number of valid sub-arrays
        count = 0

        # Check if the first window satisfies the condition
        if window_sum >= target:
            count += 1

        # Slide the window from index k to the end
        for right in range(k, len(arr)):

            # Add the new element entering the window
            window_sum += arr[right]

            # Remove the old element leaving the window
            window_sum -= arr[right - k]

            # Check if the current window satisfies the condition
            if window_sum >= target:
                count += 1

        # Return the total number of valid sub-arrays
        return count