'''
给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。
返回 只删除一个 子数组可获得的 最大得分 。
如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。

策略：（1）滑动窗口 + 哈希  （2）可以进一步优化，处理前缀和，不再使用哈希集求和
'''
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pre = set()
        start, ans = 0, 0
        for i in range(len(nums)):
            if nums[i] not in pre:
                pre.add(nums[i])
                ans = max(ans, sum(pre))
            else:
                while start < i:
                    if nums[start] == nums[i]:
                        start += 1
                        break
                    else:
                        pre.remove(nums[start])
                        start += 1
        return ans

    def maximumUniqueSubarray_pre(self, nums: List[int]) -> int:
        pre = set()
        start, ans, temp = 0, 0, 0
        pre_sum = [0]
        for i in range(len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])
            if nums[i] not in pre:
                pre.add(nums[i])
                ans = max(pre_sum[i + 1] - pre_sum[start], ans)
            else:
                while start < i:
                    if nums[start] == nums[i]:
                        start += 1
                        break
                    else:
                        pre.remove(nums[start])
                        start += 1
        return ans


solution = Solution()
nums = [449, 154, 934, 526, 429, 732, 784, 909, 884, 805, 635, 660, 742, 209, 742, 272, 669, 449, 766, 904, 698, 434, 280, 332, 876, 200, 333, 464, 12, 437, 269, 355, 622, 903, 262, 691, 768, 894, 929, 628, 867, 844, 208, 384, 644, 511, 908, 792, 56, 872, 275, 598, 633, 502, 894, 999, 788, 394, 309, 950, 159, 178, 403, 110, 670, 234, 119, 953, 267, 634,
        330, 410, 137, 805, 317, 470, 563, 900, 545, 308, 531, 428, 526, 593, 638, 651, 320, 874, 810, 666, 180, 521, 452, 131, 201, 915, 502, 765, 17, 577, 821, 731, 925, 953, 111, 305, 705, 162, 994, 425, 17, 140, 700, 475, 772, 385, 922, 159, 840, 367, 276, 635, 696, 70, 744, 804, 63, 448, 435, 242, 507, 764, 373, 314, 140, 825, 34, 383, 151, 602, 745]
print(solution.maximumUniqueSubarray_pre(nums))
