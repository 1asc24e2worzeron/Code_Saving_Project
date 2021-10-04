class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        maxNum = -101
        for i in range(0, len(nums)):
            if nums[i] > maxNum:
                nums[count] = nums[i]
                maxNum = nums[i]
                count += 1
                
        nums = nums[:count]
        return len(nums)