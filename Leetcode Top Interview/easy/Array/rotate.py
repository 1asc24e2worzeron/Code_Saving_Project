class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        realK = k % len(nums)
        separatePoint = len(nums) - realK
        part1, part2 = nums[separatePoint:len(nums)], nums[:separatePoint]
        
        while nums:
            nums.pop()
        
        nums.extend(part1)
        nums.extend(part2)