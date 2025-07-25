class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        k = 0
        while (i < len(nums)):
            
            if i + 1 != len(nums) and nums[i] == nums[i + 1]:
                nums.remove(nums[i])
            else:
                i = i + 1
                k = k + 1

        return(k)

                
            