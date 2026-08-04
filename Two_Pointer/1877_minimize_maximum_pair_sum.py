
# LeetCode 1877 - Minimize Maximum Pair Sum in Array
# Difficulty: Medium

# Input: nums = [3,5,2,3]
# Output: 7
# Explanation: The elements can be paired # up into pairs (3,3) and (5,2).
# The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.


# Language: Python 3
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Approach: Greedy + Sorting + Two Pointers


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        ans = 0

        while left < right:
            ans = max(ans, nums[left] + nums[right])
            left += 1
            right -= 1

        return ans