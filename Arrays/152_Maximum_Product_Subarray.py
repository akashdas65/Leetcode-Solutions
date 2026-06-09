# LeetCode 152 - Maximum Product Subarray
# Time Complexity: O(n)
# Space Complexity: O(1)

class solution:
  def maxproduct(self,nums):
    cur_max=nums[0]
    cur_min=nums[0]
    ans=nums[0]

    for i in range(1,len(nums)):
      num=nums[i]
      temp_max=max(num,cur_max*num,cur_min*num)
      cur_min=min(num,cur_max*num,cur_min*num)
      cur_max=temp_max

      ans=max(ans,cur_max)

    return ans
