class Solution:

    # 自己的
    def singleNumber(self, nums: List[int]) -> int:
        
        numSet = set()
        for num in nums:
            if num not in numSet:
                numSet.add(num)
            else:
                numSet.remove(num)
        
        return numSet.pop()