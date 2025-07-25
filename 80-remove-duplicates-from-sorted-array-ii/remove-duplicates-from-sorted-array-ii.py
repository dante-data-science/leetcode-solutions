class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        k = len(nums)
        while (i < len(nums)):
            
            if i + 2 >= len(nums):
                break
            if nums[i] == nums[i + 1] and nums[i] == nums[i + 2]:
                nums.remove(nums[i])
                k = k - 1
            else:
                i = i + 1
                
        return(k)