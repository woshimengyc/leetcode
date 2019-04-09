class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = list()
        nums_len = len(nums)
        if nums_len < 3:
            return result
        l, r, dif = 0, 0, 0
        nums.sort()
        for i in range(nums_len - 2):
            if nums[i] > 0: 
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l = i + 1
            r = nums_len - 1
            dif = -nums[i]
            while l < r:
                if nums[l] + nums[r] == dif:
                    result.append([nums[l], nums[r], nums[i]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < dif:
                    l += 1
                else:
                    r -= 1
        
        return result
