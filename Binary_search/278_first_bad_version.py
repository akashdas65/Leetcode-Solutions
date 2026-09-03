# LeetCode 278 - First Bad Version

# Category: Binary Search

# Approach:
# We use binary search because once a version is bad, all versions after it
# are also bad. So we search for the first version where isBadVersion()
# returns True.

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left