'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

策略: 
'''
from typing import List


class Solution:
    def save_sum(self, sum1, sum2, target):
        return sum1 if abs(sum1 - target) < abs(sum2 - target) else sum2

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        ans = float('inf')
        for i in range(l - 2):
            j, k = i + 1, l - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k: 
                temp_sum = nums[i] + nums[j] + nums[k]
                ans = self.save_sum(ans, temp_sum, target)
                if temp_sum < target:
                    while j < k and nums[j + 1] == nums[j]:
                        j += 1
                    j += 1
                elif temp_sum > target:
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1
                    k -= 1
                else:
                    return target
            
        return ans

nums = [0,1,2]
target = 3

s = Solution()
print(s.threeSumClosest(nums, target))