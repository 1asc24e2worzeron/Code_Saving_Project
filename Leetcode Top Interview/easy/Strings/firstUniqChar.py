class Solution:
    # 自己的，不用既有函式，改用自寫最佳邏輯
    # runtime (beats) 85.44%, memory 71.02%
    # 96ms, 14.3MB
    # 順帶一提，如果用 for i in range 取代 for ch in s，
    # memory 可以更省，但會變慢一點
    def firstUniqChar(self, s: str) -> int:
        charCount = set()
        repeatSet = set()
        for ch in s:
            if ch in charCount:
                repeatSet.add(ch)
            else:
                charCount.add(ch)
        
        for i in range(len(s)):
            if s[i] not in repeatSet:
                return i
        return -1
    # 自己的，嘗試利用既有函式，結果 runtime 6.27%
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1
    # 範例程式中接近最快的(56ms)，又是 Counter
    def firstUniqChar(self, s: str) -> int:
        countDict = dict(Counter(s))
        for key, item in countDict.items():
            if item == 1:
                return s.index(key)
        return -1