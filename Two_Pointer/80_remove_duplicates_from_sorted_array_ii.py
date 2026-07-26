# LeetCode 80 - Remove Duplicates from Sorted Array II
# Category: Array, Two Pointers

# Approach:
# Since the array is sorted, duplicates appear consecutively.
# Maintain a pointer `k` that represents the position to place the next valid element.
# The first two elements are always allowed.
# For each remaining element:
# - If it is different from the element two positions before `k`,
#   place it at index `k` and increment `k`.
# - Otherwise, skip it because it would appear more than twice.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k