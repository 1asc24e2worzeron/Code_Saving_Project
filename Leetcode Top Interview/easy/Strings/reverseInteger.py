class Solution:
    # 自己的，看完範例後發現 math.pow 可以用 ** 取代
    # 所以又修正上傳了一次，超過 91.96% 的上傳紀錄
    # 採用效率至上的邏輯
    def reverse(self, x: int) -> int:
        if(x > 0):
            reversedX = int(str(x)[::-1])
            if reversedX > 2**31 - 1:
                return 0
            return reversedX
        else:
            reversedX = -int(str(-x)[::-1])
            if reversedX < -2**31:
                return 0
            return reversedX