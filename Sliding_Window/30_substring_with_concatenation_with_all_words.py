# LeetCode 30 - Substring with Concatenation of All Words

# Approach:
# Use a hash map to store the frequency of each word.
# For every possible starting index, check words of fixed length.
# Count the words seen in the current window.
# If all words match the required frequency, add the index to the answer.

from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        window_len = word_len * total_words

        word_count = Counter(words)
        ans = []

        for i in range(len(s) - window_len + 1):

            seen = {}

            for j in range(total_words):

                start = i + j * word_len
                word = s[start:start + word_len]

                if word not in word_count:
                    break

                seen[word] = seen.get(word, 0) + 1

                if seen[word] > word_count[word]:
                    break

            else:
                ans.append(i)

        return ans

# Time Complexity: O(n × m)
# Space Complexity: O(m)