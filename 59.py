class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = []
        for i in range(n):
            m.append([0] * n)
        di = 0
        dj = 1
        i, j = 0, 0
        for num in range(n * n):
            m[i][j] = num + 1
            if m[(i + di) % n][(j + dj) % n] != 0:
                di, dj = dj, -di
            i += di
            j += dj
        return m
