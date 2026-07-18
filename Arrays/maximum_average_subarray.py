# LeetCode 643 - Maximum Average Subarray I

# Category: Array, Sliding Window

# Approach:
# Calculate the sum of the first window of size k. Then slide the window
# by adding the new element and removing the leftmost element. Track the
# maximum window sum and return its average.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
