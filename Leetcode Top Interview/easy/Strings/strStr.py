# 嗯對，又是入門題，頂多對新手造成挑戰
class Solution:
    # 自寫，方法一
    # Runtime: 58 ms (49.38%), Memory Usage: 14.2 MB (92.18%)
    # 我懶得吐槽了
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        
    # 非自寫 (12ms)
    # 最快的，跟我想像的差不多，用判斷式排除例外狀況
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1
        
    # 自寫，方法二
    # Runtime: 148 ms (22.73%), Memory Usage: 14.2 MB (92.18%)
    # 暴力手刻就算邏輯最佳化還是慢得跟烏龜一樣，這是其中最快的寫法
    def strStr(self, haystack: str, needle: str) -> int:
        
        checkRange = len(needle)
        if checkRange == 0:
            return 0
        
        diff = len(haystack)-len(needle)+1
        if diff < 0:
            return -1
        
        for i in range(diff):
            if haystack[i:i+checkRange] == needle:
                return i
        return -1
        
    # 半自寫，方法三
    # Runtime: 155 ms (20.01%), Memory Usage: 14.3 MB (81.28%)
    # 為了下面的方法三改實驗放上來做對照組
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        if needle in haystack:
            diff = len(haystack)-len(needle)+1
            checkRange = len(needle)
            for i in range(diff):
                if haystack[i:i+checkRange] == needle:
                    return i
        return -1
    
    # 半自寫，方法三改
    # Runtime: 134 ms (27.26%), Memory Usage: 14.2 MB (97.77%)
    # 好奇如我當然要試試不創變數會不會比較快，結果是會
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        if needle in haystack:
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1