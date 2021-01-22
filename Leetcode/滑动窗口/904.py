'''
在一排树中，第 i 棵树产生 tree[i] 型的水果。
你可以从你选择的任何树开始，然后重复执行以下步骤：

把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
移动到当前树右侧的下一棵树。如果右边没有树，就停下来。

策略：滑动窗口
'''

from typing import List
import collections

class Solution:
    
    def totalFruit(self, tree: List[int]) -> int:
        ans , i = 0, 0
        all_type = collections.defaultdict(lambda: 0)
        for j in range(len(tree)):
            all_type[tree[j]] += 1
            if len(all_type) >= 3:
                all_type[tree[i]] -= 1
                if all_type[tree[i]] == 0:
                    del all_type[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans

solution = Solution()
print(solution.totalFruit())