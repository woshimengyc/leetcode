class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        ans = []
        candidates.sort()
        def backtrack(t,target):
            if target == 0:
                ans.append(temp[:])
                return 
            temp.append(0)
            for i in range(t,len(candidates)):
                if candidates[i]>target:
                    break
                temp[-1]=candidates[i]
                backtrack(i,target-candidates[i])
            temp.pop()
        backtrack(0,target)
        return ans
