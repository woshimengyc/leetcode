class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_hash = {}
        ans = []
        for i in range(len(nums)):
            num_hash[nums[i]] = num_hash.get(nums[i],0) + 1
        nums=sorted(list(num_hash.keys()))
        if 0 in num_hash and num_hash[0]>=3:
            ans.append([0,0,0])
        for i,num in enumerate(nums):
            for k in nums[i+1:]:
                if 2*num + k == 0 and num_hash[num]>=2:
                    ans.append([num,num,k])
                if 2*k + num ==0 and num_hash[k]>=2:
                    ans.append([k,k,num])
                s = 0-num-k
                if s in num_hash and s>k:
                    ans.append([num,k,s])
        return ans
