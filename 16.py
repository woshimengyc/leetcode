import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        dist = sys.maxsize
        nums.sort()
        for a in range(len(nums)-1):
            b = a + 1
            c = len(nums)-1
            while c>b:
                delta = target - nums[a] - nums[b] - nums[c]
                dist_now= abs(delta)
                if dist_now < dist:
                    ans = nums[a]+nums[b]+nums[c]
                    dist = dist_now
                if delta < 0:
                    c-=1
                else:
                    b+=1
        return ans
