class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m==0:
            return False
        n = len(matrix[0])
        if n==0:
            return False
        tr = 0
        for i in range(m):
            if matrix[i][0]<=target:
                tr = i
                continue
            break
        l = 0
        r = len(matrix[0])-1
        while l<=r:
            mid = (l+r)//2
            if matrix[tr][mid] == target:
                return True
            elif matrix[tr][mid] <target:
                l=mid+1
            elif matrix[tr][mid] >target:
                r=mid-1
        return False
