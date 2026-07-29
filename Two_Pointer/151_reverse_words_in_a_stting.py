# LeetCode 151 - Reverse Words in a String

# Solution 1: Using split() and join()

# Approach:
# 1. Use split() to divide the string into words.
#    - Removes leading/trailing spaces.
#    - Treats multiple spaces as a single separator.
# 2. Reverse the list of words.
# 3. Join the reversed words with a single space.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])