class Solution:
    
    # 自己的，試試看 list.count 有沒有比較快，答案是沒有
    # 程式碼倒是數一數二短的
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
            
    # 一樣是能看懂的裡面最快的，順便優化一下
    # 同時這也是我一開始的想法，但每次最佳通常邏輯都會輸一些怪方法，所以最初沒有用
    # 嘗試交上去後還是很慢，可見要看伺服器的狀態
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 0:
            i = 0
            for j in range(len(nums)):
                if nums[j] != 0:
                    if j != i:
                        nums[i], nums[j] = nums[j], nums[i]
                    i += 1
        return