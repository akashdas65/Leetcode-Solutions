# LeetCode 217 - Contains Duplicate
# Category: Array, Hash Set

# Approach:
# Use a hash set to keep track of the elements seen so far. Traverse the
# array, and if the current element already exists in the set, return True.
# Otherwise, add it to the set. If no duplicates are found, return False.

# Time Complexity: O(n)
# Space Complexity: O(n)

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
      
