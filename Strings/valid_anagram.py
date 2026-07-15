# LeetCode 242 - Valid Anagram

# Approach:
# Compare the lengths of both strings. Use a frequency array of size 26 to count characters.
# Increase the count for each character in the first string and decrease it for the corresponding character in the second string. 
# If all frequencies become zero, the strings are anagrams.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for num in count:
            if num != 0:
                return False

        return True
