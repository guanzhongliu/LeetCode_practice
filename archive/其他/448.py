'''
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

策略：原地修改，遍历数组nums，每遇到一个x，就让nums[x-1]增加n，由于nums中原本所有数均在范围[1, n]，所以在遍历第一遍后，只需找哪些数字未大于n即可知道其未出现过
     让数组本身充当哈希表
'''
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            temp = (nums[i] - 1) % n
            nums[temp] += n
        ans = [i + 1 for i in range(n) if nums[i] <= n]
        
        return ans

solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))