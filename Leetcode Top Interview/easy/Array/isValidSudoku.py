class Solution:
    
    # 自己的，set version
    # 順便學到 Python 有整除符號 //，不用每次都 int(x/y)
    # 更快的寫法是預建好 9*3 個 set，過程不清空，順便省去照順序檢查9個 grid 必須的計算
    # 再更快是用不含 "." 的 unit list 做 len(set(unit)) == len(unit) 判斷
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        currSets = [set(), set(), set()]
        
        for i in range(9):
            
            for j in range(9):
                subBoxes = [board[i//3*3 + j//3][i%3*3 + j%3], board[i][j], board[j][i]]
                for k in range(3):
                    if subBoxes[k] != ".":
                        if subBoxes[k] in currSets[k]:
                            return False
                        else:
                            currSets[k].add(subBoxes[k])
            
            if i == 8:
                return True
            
            for j in range(3):
                currSets[j].clear()
    
    # 自己的，dict version，勉強在時間內
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        validDict = {
            "1": False, "2": False, "3": False,
            "4": False, "5": False, "6": False,
            "7": False, "8": False, "9": False
        }
        validDicts = [copy.deepcopy(validDict), copy.deepcopy(validDict), copy.deepcopy(validDict)]
        
        for i in range(9):
            
            for j in range(9):
                subBoxes = [board[int(i/3)*3 + int(j/3)][i%3*3 + j%3], board[i][j], board[j][i]]
                for k in range(3):
                    if subBoxes[k] in validDicts[k]:
                        if validDicts[k][subBoxes[k]]:
                            return False
                        else:
                            validDicts[k][subBoxes[k]] = True
            
            if i == 8:
                return True
            
            for j in range(3):
                for key in validDicts[j]:
                    validDicts[j][key] = False
                    