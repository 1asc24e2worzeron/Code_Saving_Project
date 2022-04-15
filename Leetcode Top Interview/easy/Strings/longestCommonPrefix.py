# 啊對我又有時間了，Ahhhh...
class Solution:
    # 自寫，方法一
    # Runtime: Runtime: 33 ms (90.19%), Memory Usage: 13.9 MB (53.18%)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            # 每次開始把比較範圍限縮在 prefix / 目標 中的最小長度
            # 同時把 prefix 壓成此長度，避免 len(目標) == 0 時不比較，
            # 順便省去 j 迴圈中 len(prefix) > len(目標) 且沒不同時，擷取最短用的檢查
            strRange = min(len(prefix), len(strs[i]))
            prefix = prefix[:strRange]
            for j in range(strRange):
                # 有不同就擷取後退出
                if prefix[j] != strs[i][j]:
                    prefix = strs[i][:j]
                    break
        return prefix
    
    # 自寫，方法一改
    # Runtime: 28 ms (98.62%), Memory Usage: 14 MB (53.18%)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 先算整體最小長度，把 prefix 長度跟比較範圍都壓在其內，prefix 長度連逐次下壓都免了
        minLen = min(map(len, strs))
        prefix = strs[0][:minLen]
        for i in range(1, len(strs)):
            # prefix 如果比整體最小長度短，就把比較範圍再往下壓
            strRange = min(len(prefix), minLen)
            for j in range(strRange):
                # 有不同就擷取後退出
                if prefix[j] != strs[i][j]:
                    prefix = strs[i][:j]
                    break
        return prefix
