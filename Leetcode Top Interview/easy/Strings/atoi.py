class Solution:

    # 自寫，方法一
    # Runtime: 46 ms (47.28%), Memory Usage: 13.9 MB (99.78%)
    def myAtoi(self, s: str) -> int:
        # 判斷是否存在符合要求、可被轉為整數的片段
        # 也就是「在開頭處有或許帶有 leading space 的整數」
        # 無則回傳0，有則轉換成整數
        reNum = re.search("^( *[-+]?[0-9]+)", s)
        if reNum is None:
            return 0
        num = int(reNum.group())
        # 超出範圍 --> 回傳正/負極值
        # 沒超出範圍 --> 回傳轉換後的數字部分
        if num > 2**31 - 1:
            return 2**31 - 1
        if num < -2**31:
            return -2**31
        return num
        
    # 自寫，方法一改
    # Runtime: 36 ms (78.50%), Memory Usage: 13.9 MB (98.22%)
    def myAtoi(self, s: str) -> int:
        # 有辦法直接轉換的，直接交給 Python 內建轉換
        try:
            num = int(s)
        except:
            reNum = re.search("^( *[-+]?[0-9]+)", s)
            if reNum is None:
                return 0
            num = int(reNum.group())
        # 寫法不變
        if num > 2**31 - 1:
            return 2**31 - 1
        if num < -2**31:
            return -2**31
        return num
        
    # 最快的方法 (12ms)是依照題目要求暴力手刻上半部
    # 沒什麼好寫的，甚至丟個別測資速度也是 32~40ms 左右，就不放上來了
    # 大概又是伺服器效率問題
    
    # 然後我發現上面寫 Easy Collection，但根本不是指「題目是 Easy 難度」
    # 被哄著亂玩了一大堆 Medium 題...算了反正也沒多吃力