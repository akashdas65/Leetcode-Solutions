# 151. Reverse Words in a String

# **Difficulty:** Medium

## Problem Statement

# Given a string `s`, reverse the order of the words.

A **word** is a sequence of non-space characters. The words in `s` may contain leading, trailing, or multiple spaces between them.

Return a string with the words in reverse order, separated by a **single space**.

---

## Example

**Input:**
```text
s = "the sky is blue"
```

**Output:**
```text
"blue is sky the"
```

---

# Solution 1: Using Two Pointers

## Approach (Step by Step)

1. Split the string into individual words using `split()`.
2. Reverse the list using the two-pointer technique.
3. Join the reversed words using `" ".join()`.

### Python Solution

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        left, right = 0, len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`

---

# Solution 2: Pythonic Approach

## Approach (Step by Step)

1. Split the string into words using `split()`.
2. Reverse the list using slicing (`[::-1]`).
3. Join the reversed words using `" ".join()`.

### Python Solution

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`