# LeetCode 2351 - First Letter to Appear Twice
# Pattern: Hash Set
# Difficulty: Easy
#
# Question:
# Given a string s consisting of lowercase English letters,
# return the first letter to appear twice.
#
# A letter is considered to appear twice when it occurs for
# the second time in the string.
#
# Example:
# Input:  s = "abccbaacz"
# Output: "c"
#
# Explanation:
# The letter 'c' appears for the second time before any other
# letter appears for the second time.
#
# Approach:
# 1. Create a set to store characters that have already appeared.
# 2. Traverse the string from left to right.
# 3. If the current character is already in the set,
#    it is the first character to appear twice.
# 4. Return that character immediately.
# 5. Otherwise, add the character to the set.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def repeatedCharacter(self, s: str) -> str:

        # Create a set to store characters that have appeared
        seen = set()

        # Traverse through every character in the string
        for char in s:

            # Check if the character has already appeared
            if char in seen:

                # Return the first character that appears twice
                return char

            # Add the current character to the set
            seen.add(char)