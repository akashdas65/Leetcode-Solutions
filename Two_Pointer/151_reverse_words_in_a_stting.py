# LeetCode 151 - Reverse Words in a String
# Pattern: Two Pointers
# Difficulty: Medium
#
# Question:
# Given a string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters.
# The words in the input string may be separated by multiple spaces.
# Return a string with the words in reverse order,
# separated by a single space.
#
# Example:
# Input:  s = "the sky is blue"
# Output: "blue is sky the"
#
# Approach:
# 1. Start from the end of the string.
# 2. Skip all spaces.
# 3. Find each word.
# 4. Add each word to the result.
# 5. Continue until the beginning of the string.
# 6. Join all words using a single space.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def reverseWords(self, s: str) -> str:

        # Store the reversed words
        result = []

        # Start from the last character
        right = len(s) - 1

        # Traverse the string from right to left
        while right >= 0:

            # Skip spaces
            while right >= 0 and s[right] == ' ':
                right -= 1

            # Stop if no characters are left
            if right < 0:
                break

            # Store the end index of the word
            end = right

            # Move left until a space is found
            while right >= 0 and s[right] != ' ':
                right -= 1

            # Extract the current word
            word = s[right + 1:end + 1]

            # Add the word to the result
            result.append(word)

        # Join all words with one space
        return ' '.join(result)