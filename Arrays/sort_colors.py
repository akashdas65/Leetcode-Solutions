# LeetCode 75 - Sort Colors
# Category: Array, Two Pointers

# Approach:
# Use the Dutch National Flag algorithm with three pointers:
# - low: points to the next position for 0
# - mid: traverses the array
# - high: points to the next position for 2
#
# If nums[mid] == 0:
#   Swap nums[low] and nums[mid], then increment both low and mid.
# If nums[mid] == 1:
#   It is already in the correct position, so increment mid.
# If nums[mid] == 2:
#   Swap nums[mid] and nums[high], then decrement high.
#   Do not increment mid because the swapped element needs to be checked.
#
# This sorts the array in a single pass without using any built-in sorting.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            # If current element is 0
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            # If current element is 1
            elif nums[mid] == 1:
                mid += 1

            # If current element is 2
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
      
