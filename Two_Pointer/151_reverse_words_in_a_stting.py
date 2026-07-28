# LeetCode 344 - Reverse String

# Problem Statement:
# Write a function that reverses a string.
# The input string is given as an array of characters s.
# You must modify the input array in-place with O(1) extra memory.

# Example:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


# Solution 1: Two Pointer Approach

# Approach:
# Use two pointers.
# One pointer starts from the beginning and the other from the end.
# Swap the characters at both pointers.
# Move the left pointer forward and the right pointer backward.
# Continue until the pointers meet.

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


# Solution 2: Using Built-in Reverse Method

# Approach:
# Python provides a built-in reverse() method for lists.
# It reverses the list in-place without creating a new list.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

# Time Complexity: O(n)
# Space Complexity: O(1)