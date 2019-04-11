class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        di = [0,1,0,-1]
        dj = [1,0,-1,0]
        d = 0
        i,j =0,0
        if matrix ==[]:
            return res
        for n in range(len(matrix)*len(matrix[0])):
            res.append(matrix[i][j])
            matrix[i][j] = 0.5
            if matrix[(i+di[d])%len(matrix)][(j+dj[d])%len(matrix[0])] == 0.5: 
                d = (d+1)%4
            i+=di[d]
            j+=dj[d]
        return res
