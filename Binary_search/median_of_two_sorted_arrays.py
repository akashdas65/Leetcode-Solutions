# LeetCode 4 - Median of Two Sorted Arrays

# Category: Array, Binary Search

# Approach:
# Perform binary search on the smaller array to find the correct partition
# of both arrays. The left partition contains half of the elements and all
# elements in the left partition are less than or equal to those in the
# right partition. Compute the median based on the partition.

# Time Complexity: O(log(min(m, n)))
# Space Complexity: O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        left, right = 0, x

        while left <= right:
            partitionX = (left + right) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float("inf") if partitionX == x else nums1[partitionX]

            maxLeftY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float("inf") if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)

            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1
