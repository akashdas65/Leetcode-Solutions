# LeetCode 283 - Move Zeroes

# Approach:
# Use two pointers.
# Pointer k stores the position where the next non-zero element should be placed.
# Traverse the array with i.
# If nums[i] is non-zero, swap nums[i] with nums[k] and increment k.
# This keeps all non-zero elements in order and moves zeros to the end.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        left = 0

        for right in range(len(nums)):

            if nums[right] != 0:

                nums[left], nums[right] = nums[right], nums[left]

                left += 1

# Time Complexity: O(n)
# Space Complexity: O(1)