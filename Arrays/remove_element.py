# LeetCode 27 - Remove Element
# Approach:
# Use the Two Pointers technique. One pointer (i) traverses the array, while another pointer (k) keeps track of the position where the next valid element should be placed. If the current element is not equal to val, copy it to nums[k] and increment k. After the traversal, the first k elements contain all the required elements, and k is returned as the new length.

# Time Complexity: O(n)
# Space Complexity: O(1)

class solution:    
    def removeelements(self,nums,val):
        k=0
        for i in range(len(nums)):
            if nums[k] != val:
                nums[i]=nums[k]
                k+=1
        return k
                
    
