'''
当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：

若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。

返回 A 的最大湍流子数组的长度。

策略：（1）遍历，依照可能的情况进行判断     （2）优化一下判断方式
'''
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right, ans, temp = 0, 1, 1, 1
        while right < len(arr):
            if right == left + 1:
                if arr[right] == arr[left]:
                    left = right
                    right += 1
                    temp = 1
                else:
                    temp += 1
                    right += 1
            elif ((arr[right] > arr[right - 1]) and (arr[right - 1] < arr[right - 2])) or ((arr[right] < arr[right - 1]) and (arr[right - 1] > arr[right - 2])):
                temp += 1
                right += 1
            else:
                left = right - 1
                temp = 1
            ans = max(ans, temp)
        return ans

    def maxTurbulenceSize_official(self, arr: List[int]) -> int:
        left, right, ans = 0, 1, 1
        pre = False
        while right < len(arr):
            current = arr[right - 1] < arr[right]
            if current == pre:
                left = right - 1
            if arr[right - 1] == arr[right]:
                left = right
            right += 1
            ans = max(ans, right - left)
            pre = current
        return ans
