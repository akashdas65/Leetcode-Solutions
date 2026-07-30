#268. Missing Number

# Given an array nums containing n #distinct numbers in the range [0, n], #return the only number in the range that #is missing from the array.

#Example 1:

#Input: nums = [3,0,1]

#Output: 2

#Explanation:

#n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums


# Solution 2: XOR (Optimal)

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = len(nums)

        for i in range(len(nums)):
            xor ^= i ^ nums[i]

        return xor


# Solution 1: Sum Formula (Optimal)

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # Sum of numbers from 0 to n
        expected_sum = n * (n + 1) // 2

        # Sum of all elements in the array
        actual_sum = sum(nums)

        # The difference is the missing number
        return expected_sum - actual_sum

#Time Complexity = O(n)
#Space Complexity = O(1)