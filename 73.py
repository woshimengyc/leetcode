class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zr = []
        zc = []
        for i in range(len(matrix)):
            # if i in zr:
            #     continue
            for j in range(len(matrix[0])):
                # if j in zc:
                #     continue
                if matrix[i][j]==0:
                    if i not in zr:
                        zr.append(i)
                    if j not in zc:
                        zc.append(j)
        for r in zr:
            for j in range(len(matrix[0])):
                matrix[r][j]=0
        for c in zc:
            for i in range(len(matrix)):
                matrix[i][c]=0
        return
