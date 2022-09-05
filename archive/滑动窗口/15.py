'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

策略：双指针，先排序，然后在固定i时，用j和l遍历所有搭配
'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        i = 0
        nums.sort()
        res = []
        while i < len(nums) - 2:
            j, l = i + 1, len(nums) - 1
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            while j < l:
                if nums[i] + nums[j] + nums[l] == 0:
                    res.append([nums[i], nums[j], nums[l]])
                    while j < l and nums[j] == nums[j+1]:
                        j += 1
                    while j < l and nums[l-1] == nums[l]:
                        l -= 1
                    j += 1
                    l -= 1
                elif nums[i] + nums[j] + nums[l] < 0:
                    j += 1
                else:
                    l -= 1
            i += 1
        return res

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))