class Solution:
    # 不知道放這種題有什麼意義
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            swap = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = swap