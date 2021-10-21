class Solution:
    # 自己的，沒什麼好講，連紀錄都少到沒有顯示出來的題目
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        tempMatrix = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[j][len(matrix)-1-i] = tempMatrix[i][j]