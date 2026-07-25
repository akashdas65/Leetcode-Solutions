# LeetCode 3090 - Maximum Length Substring With Two Occurrences

# Approach:
# Use the sliding window technique with two pointers.
# Store the frequency of each character in a dictionary.
# Expand the window by moving the right pointer.
# If any character appears more than twice, shrink the window from the left.
# Update the maximum valid window length.

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        left = 0
        count = {}
        ans = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans

# Time Complexity: O(n)
# Space Complexity: O(1)