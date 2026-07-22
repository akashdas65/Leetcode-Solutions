# LeetCode 3 - Longest Substring Without Repeating Characters

# Category: String, Sliding Window, Hash Set

# Approach:
# Use a sliding window with two pointers and a hash set.
# Expand the window by moving the right pointer. If a duplicate
# character is found, shrink the window from the left until the
# duplicate is removed. Track the maximum window size.

# Time Complexity: O(n)
# Space Complexity: O(min(n, charset))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
