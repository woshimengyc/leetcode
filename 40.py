class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        temp = []
        def backtrack(t,target):
            if target == 0:
                ans.append(temp[:])
                return
            temp.append(0)
            for i in range(t,len(candidates)):
                if candidates[i] > target:
                    break
                temp[-1]=candidates[i]
                backtrack(i+1,target-candidates[i])
            temp.pop()
        backtrack(0,target)
        ans2 =[]
        for i in ans:
            if i not in ans2:
                ans2.append(i)
        return ans2
