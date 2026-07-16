# LeetCode 217 - Contains Duplicate
# Category: Array, Hash Set

# Approach:
# Use a hash set to keep track of the elements seen so far. Traverse the
# array, and if the current element already exists in the set, return True.
# Otherwise, add it to the set. If no duplicates are found, return False.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
