
# Solution 2: Using Built-in Reverse Method

# Approach:
# Python provides a built-in reverse() method for lists.
# It reverses the list in-place without creating a new list.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

# Time Complexity: O(n)
# Space Complexity: O(1)