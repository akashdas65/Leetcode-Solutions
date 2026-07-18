# LeetCode 53 - Maximum Subarray

# Category: Array, Dynamic Programming (Kadane's Algorithm)

# Approach:
# Traverse the array while keeping track of the maximum sum ending at
# the current position. If the current sum becomes smaller than the
# current element, start a new subarray from the current element.
# Update the overall maximum sum during each iteration.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
