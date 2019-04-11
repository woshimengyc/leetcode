class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_now = 0
        for i in range(len(nums)-1):
            max_now = max(max_now -1,nums[i])
            if nums[i]==0 and max_now ==0:
                return False
        return True
