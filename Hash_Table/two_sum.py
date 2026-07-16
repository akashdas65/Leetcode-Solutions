# LeetCode 1 - Two Sum
# Category: Array, Hash Table

# Approach:
# Use a hash map to store each number and its index. For every element,
# calculate its complement (target - current number). If the complement
# already exists in the hash map, return the two indices. Otherwise,
# store the current number and its index in the hash map.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
