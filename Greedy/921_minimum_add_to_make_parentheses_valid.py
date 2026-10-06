# LeetCode 921 - Minimum Add to Make Parentheses Valid
#
# Category: Stack / Greedy
#
# Question:
# Given a string s of '(' and ')', return the minimum number
# of parentheses that must be added to make the string valid.
#
# Example 1:
# Input:  s = "())"
# Output: 1
#
# Example 2:
# Input:  s = "((("
# Output: 3
#
# Example 3:
# Input:  s = "()"
# Output: 0
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        ans = 0

        for ch in s:
            if ch == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    ans += 1

        return ans + open