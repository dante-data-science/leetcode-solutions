class Solution(object):
    def moveZeroes(self, nums):

        j = 0
        #loops through indicies of nums
        for i in range(0, len(nums)):
            #If nums[j] equals zero, remove element, then add zero after the last value 
            if nums[j] == 0:
                nums.pop(j)
                nums.extend([0])
            else:
                #increments j 
                j += 1
                   
        return nums
            
        