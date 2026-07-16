# LeetCode 219 - Contains Duplicate II

# Category: Array, Hash Table

# Approach:
# Use a hash map to store the most recent index of each element.
# While traversing the array, if the current element already exists
# in the hash map and the difference between the current index and
# the previous index is less than or equal to k, return True.
# Otherwise, update the element's index in the hash map.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True

            seen[num] = i

        return False
