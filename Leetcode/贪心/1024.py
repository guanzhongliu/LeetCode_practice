'''
你将会获得一系列视频片段，这些片段来自于一项持续时长为 T 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。
视频片段 clips[i] 都用区间进行表示：开始于 clips[i][0] 并于 clips[i][1] 结束。我们甚至可以对这些片段自由地再剪辑，例如片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。
我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。

策略：（1）排序 + 贪心， 思路就是尽可能选择右端点远的，然后进行模拟 O(NlogN)
     （2）贪心         记录每个左端点能到达的最远距离
'''
from typing import List

def compare(a: List, b: List) -> bool:
    if a[0] == b[0]:
        return a[1] < b[1]
    else:
        return a[0] < b[0]

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda x:(x[0],-x[1]))
        temp = clips[0]
        if T == 0:
            return 0
        if temp[0] != 0:
            return -1
        elif temp[1] >= T:
            return 1
        broad = last = temp[1]
        cnt = 1
        for i in range(1, len(clips)):
            if clips[i][0] <= last:
                broad = max(broad, clips[i][1])
                if broad >= T:
                    return cnt + 1
            elif broad >= clips[i][0]:
                cnt += 1
                last = broad
                broad = max(broad, clips[i][1])
            elif broad < clips[i][0]:
                return -1
        if  broad < T:
            return -1
        elif last < T:
            cnt += 1

        return cnt 
    
    def videoStitching_official(self, clips: List[List[int]], T: int) -> int:
        maxn = [0] * T
        last = ret = pre = 0
        for a, b in clips:
            if a < T:
                maxn[a] = max(maxn[a], b)  # 边界
        # 对距离空间遍历
        for i in range(T):
            last = max(last, maxn[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last
        return ret



s = Solution()
clips = [[0,1],[1,2],[1,5],[0,0]]
T = 5
print(s.videoStitching(clips, T))