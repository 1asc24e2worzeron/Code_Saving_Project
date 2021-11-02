class Solution:
    # 自己的，大家都 Counter，我也來 Counter 一下
    # 40ms(90.67%), 14.5MB(56.82%)
    # 看起來最快的幾群都是這個寫法，用 server 狀態決勝負
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)