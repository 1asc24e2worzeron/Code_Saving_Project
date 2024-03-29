class Solution(object):

    # 自己的
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numDict = {}
        for num in nums:
            if num in numDict:
                return True
            numDict[num] = True
        return False