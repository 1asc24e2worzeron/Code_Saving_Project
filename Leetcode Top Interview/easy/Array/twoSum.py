class Solution:
    # 自己的
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        for i in range(len(nums)):
            if nums[i+1:].count(target-nums[i]) > 0:
                return [i, i+1 + nums[i+1:].index(target-nums[i])]