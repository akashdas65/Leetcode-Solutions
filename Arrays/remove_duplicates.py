# LeetCode 26 - Remove Duplicates from Sorted Array

# Approach:
# Use the Two Pointers technique. One pointer (i) scans the array, while another pointer (k) keeps track of the position 
# to place the next unique element. Since the array is sorted, compare the current element with the previous one. 
# If they are different, copy the current element to nums[k] and increment k. After the traversal, the first k elements contain all the unique elements.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
