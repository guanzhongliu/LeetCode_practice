'''
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。
每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。
你的点数就是你拿到手中的所有卡牌的点数之和。
给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。

策略：需要对题目所求进行转化，实际是求长度为len(cardPoints) - k的最小子序列
'''
from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if cardPoints == k:
            return sum(cardPoints)
        minTotal = total = sum(cardPoints[:len(cardPoints) - k])
        n = len(cardPoints)

        for i in range(len(cardPoints) - k, n):
            total = total - cardPoints[i + k - n] + cardPoints[i]
            minTotal = min(minTotal, total)
        
        return sum(cardPoints) - minTotal