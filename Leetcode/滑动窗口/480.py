'''
中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
例如：
    [2,3,4]，中位数是 3
    [2,3]，中位数是 (2 + 3) / 2 = 2.5
给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。
你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

思路: (1) 官方题解：将队列分为两半，维护两个优先队列，小顶堆（large)和大顶堆(small)，small大小为的为ceil(k/2)
                  这样设计的好处在于：当二者包含的元素个数相同时，它们各自的堆顶元素的平均值即为中位数；
                  而当 small 包含的元素多了一个时，small 的堆顶元素即为中位数。这样 getMedian() 就设计完成了。
                  在成功地加入元素 num 之后，两个优先队列的元素个数可能会变得不符合要求。
                  由于我们只加入了一个元素，那么不符合要求的情况只能是下面的二者之一：
                    1. small 比 large 的元素个数多了 2 个；
                    2. small 比 large 的元素个数少了 1 个。
                  对于第一种情况，我们将 small 的堆顶元素放入 large；对于第二种情况，我们将 large 的堆顶元素放入 small，这样就可以解决问题了，
                  最后，使用延迟删除来删除要删除的数，使用哈希表记录，当其位于堆顶再做删除                
'''
import collections
from typing import List
import heapq

class DualHeap:
    def __init__(self, k: int):
        # 大根堆，维护较小的一半元素，注意 python 没有大根堆，需要将所有元素取相反数并使用小根堆
        self.small = list()
        # 小根堆，维护较大的一半元素
        self.large = list()
        # 哈希表，记录「延迟删除」的元素，key 为元素，value 为需要删除的次数
        self.delayed = collections.Counter()

        self.k = k
        # small 和 large 当前包含的元素个数，需要扣除被「延迟删除」的元素
        self.smallSize = 0
        self.largeSize = 0

    # 不断地弹出 heap 的堆顶元素，并且更新哈希表
    def prune(self, heap: List[int]):
        while heap:
            num = heap[0]
            if heap is self.small:
                num = -num
            if num in self.delayed:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    self.delayed.pop(num)
                heapq.heappop(heap)
            else:
                break
    
    # 调整 small 和 large 中的元素个数，使得二者的元素个数满足要求
    def makeBalance(self):
        if self.smallSize > self.largeSize + 1:
            # small 比 large 元素多 2 个
            heapq.heappush(self.large, -self.small[0])
            heapq.heappop(self.small)
            self.smallSize -= 1
            self.largeSize += 1
            # small 堆顶元素被移除，需要进行 prune
            self.prune(self.small)
        elif self.smallSize < self.largeSize:
            # large 比 small 元素多 1 个
            heapq.heappush(self.small, -self.large[0])
            heapq.heappop(self.large)
            self.smallSize += 1
            self.largeSize -= 1
            # large 堆顶元素被移除，需要进行 prune
            self.prune(self.large)

    def insert(self, num: int):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.smallSize += 1
        else:
            heapq.heappush(self.large, num)
            self.largeSize += 1
        self.makeBalance()

    def erase(self, num: int):
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.smallSize -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.largeSize -= 1
            if num == self.large[0]:
                self.prune(self.large)
        self.makeBalance()

    def getMedian(self) -> float:
        return float(-self.small[0]) if self.k % 2 == 1 else (-self.small[0] + self.large[0]) / 2


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DualHeap(k)
        for num in nums[:k]:
            dh.insert(num)
        
        ans = [dh.getMedian()]
        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i - k])
            ans.append(dh.getMedian())
        
        return ans