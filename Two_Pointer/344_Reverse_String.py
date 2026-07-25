# LeetCode 344 - Reverse String

# Approach:
# Use two pointers.
# One pointer starts from the beginning and the other from the end.
# Swap both characters, then move the pointers toward each other.
# Continue until both pointers meet.

class Solution:
    def reverseString(self, s: List[str]) -> None:

        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

# Time Complexity: O(n)
# Space Complexity: O(1)