class Solution:
    # 自己的，但這種題目應該沒分什麼寫法
    # 由於太基礎，感覺有點缺乏意義
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            swap = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = swap
