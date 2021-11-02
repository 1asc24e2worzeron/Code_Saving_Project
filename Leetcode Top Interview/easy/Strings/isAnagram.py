class Solution:
    # 自己的，大家都 Counter，我也來 Counter 一下
    # 40ms(90.67%), 14.5MB(56.82%)
    # 看起來最快的幾群都是這個寫法，用 server 狀態決勝負
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    # 最快的(16ms)，有點不同，減小比對物件大小加速。順便學起來
    # 看起來是先擷取其中要比對的部份，再用以創建累贅最少的 set 物件
    def isAnagram(self, s: str, t: str) -> bool:
        return set(Counter(s).items()) == set(Counter(t).items())