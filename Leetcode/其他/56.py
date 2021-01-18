'''
给出一个区间的集合，请合并所有重叠的区间。

'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        first = intervals[0][0]
        last = intervals[0][1]
        for i in range(0, len(intervals)):
            if intervals[i][0] <= last:
                if i < len(intervals) - 1:
                    last = max(intervals[i][1], last)
                else:
                    ans.append([first, max(intervals[i][1], last)])

            else:
                if i < len(intervals) - 1:
                    ans.append([first, last])
                    first = intervals[i][0]
                    last = intervals[i][1]
                else:
                    ans.append([first, last])
                    ans.append([intervals[i][0], intervals[i][1]]) 
        

        return ans


intervals = [[1, 3], [2, 3], [0, 3], [-2, 3], [9, 10]]
solution = Solution()
print(solution.merge(intervals))
