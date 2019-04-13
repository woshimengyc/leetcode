class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        l = len(word)
        self.flag = False
        did =[[0 for i in range(m)] for j in range(n)]
        if len(board)==1 and len(board[0])==1:
            return word==board[0][0]
        def dfs(i,j,curr):
            if self.flag:
                return 
            if curr == l:
                self.flag = True
                return 
            if did[i][j]==1:
                return
            if board[i][j]!=word[curr]:
                return
            did[i][j]=1
            if i>0:
                dfs(i-1,j,curr+1)
                # did[i][j]=0
            if i<n-1:
                dfs(i+1,j,curr+1)
                # did[i][j]=0
            if j>0:
                dfs(i,j-1,curr+1)
                # did[i][j]=0
            if j<m-1:
                dfs(i,j+1,curr+1)
                # did[i][j]=0
            did[i][j]=0
        for i in range(n):
            for j in range(m):
                dfs(i,j,0)
                if self.flag:
                    break
        return self.flag
