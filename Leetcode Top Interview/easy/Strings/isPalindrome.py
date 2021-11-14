class Solution:
    
    # 自寫，方法一
    # Runtime: 87 ms (11.77%), Memory Usage: 14.6 MB (60.88%)
    def isPalindrome(self, s: str) -> bool:
        
        # processing s
        processedString = ''
        for i in range(len(s)):
            if s[i].isalnum():
                processedString += s[i].lower()
                
        # judging if s is a palindrome
        for i in range(len(processedString)//2):
            if processedString[i] != processedString[-i-1]:
                return False
        return True
        
    # 自寫，方法一改
    # Runtime: 92 ms (9.74%), Memory Usage: 14.7 MB (60.88%)
    # 整體比較比逐字比較快，但由於比較了整個字串，runtime 比原版長
    def isPalindrome(self, s: str) -> bool:
        
        # processing s
        processedString = ''
        for i in range(len(s)):
            if s[i].isalnum():
                processedString += s[i].lower()
                
        # judging if s is a palindrome
        return True if processedString == processedString[::-1] else False
        
    # 自寫，方法一改二
    # Runtime: 44 ms (81.60%), Memory Usage: 14.7 MB (60.88%)
    # 結合方法一、方法一改優勢，速度兩倍
    # 順帶一提，字串長度是奇數時，中間那個會省略，是我刻意而為的
    def isPalindrome(self, s: str) -> bool:
        
        # processing s
        processed = ''
        for i in range(len(s)):
            if s[i].isalnum():
                processed += s[i].lower()
                
        # judging if s is a palindrome
        isEven = 1 - len(processed)%2
        return True if processed[:len(processed)//2] == processed[:len(processed)//2-isEven:-1] else False
        
    # 自寫，方法一改三
    # Runtime: 32 ms (98.73%), Memory Usage: 14.6 MB (60.88%)
    # 我只是想試試那個剛發現有夠累贅的簡寫，被改正常後會多快而已
    # 然後就變成最快了
    def isPalindrome(self, s: str) -> bool:
        
        # processing s
        processed = ''
        for i in range(len(s)):
            if s[i].isalnum():
                processed += s[i].lower()
                
        # judging if s is a palindrome
        isEven = 1 - len(processed)%2
        return processed[:len(processed)//2] == processed[:len(processed)//2-isEven:-1]

    # 自寫，方法二
    # Runtime: 120 ms (5%), Memory Usage: 14.7 MB (46.73%)
    # 慘不忍睹
    def isPalindrome(self, s: str) -> bool:
        
        posCount = 0
        negCount = 1
        
        while posCount + negCount < len(s):
            
            while not s[posCount].isalnum():
                posCount += 1
                if posCount + negCount >= len(s):
                    return True
            while not s[-negCount].isalnum():
                negCount += 1
                if posCount + negCount >= len(s):
                    return True
            
            if s[posCount].lower() != s[-negCount].lower():
                return False
            
            posCount += 1
            negCount += 1
        
        return True
        
    # 半自寫，方法二改
    # Runtime: 52 ms (39.60%), Memory Usage: 14.6 MB (46.73%)
    # 參考別人的寫法後，順便改良方法二了
    # 但比起不使用反轉索引、可以直接比較 l, r 判斷要不要停的寫法，
    # 還是有很大劣勢，每一輪多做2~3次加法
    # 同一個邏輯如果用正索引，會變成 28ms 左右
    def isPalindrome(self, s: str) -> bool:
        
        posCount = 0
        negCount = 1
        
        while posCount + negCount < len(s):
            
            while not s[posCount].isalnum() and posCount + negCount < len(s):
                posCount += 1
            while not s[-negCount].isalnum() and posCount + negCount < len(s):
                negCount += 1
            
            if s[posCount].lower() != s[-negCount].lower():
                return False
            
            posCount += 1
            negCount += 1
        
        return True
        
    # 非自寫，方法三，範例程式在 12ms 那一區
    # Runtime: 36 ms (96.27%), Memory Usage: 15.2 MB (33.50%)
    # 如果不先將反轉後字串存到變數 -- Runtime: 40 ms (90.91%), Memory Usage: 15.4 MB (30.58%)
    # 暫存居然比較快
    # 最快的方法，一開始看到糾結了一下先做 lower 會不會比較快，推理了一下，不會
    # set 多加 A-Z 不會花多少時間，也不會影響比對效率，但 lower 多做幾個字會，尤其多做的量跟字串長度相關
    # 順便收下 Python 的 re 技術了，未來可能有用武之地
    def isPalindrome(self, s: str) -> bool:
        
        processed = re.sub(r'[^A-Za-z0-9]+', '', s).lower()
        reverted = processed[::-1]
        
        return processed == reverted