class solution:    
    def removeelements(self,nums,val):
        k=0
        for i in range(len(nums)):
            if nums[k] != val:
                nums[i]=nums[k]
                k+=1
        return k
                
    
