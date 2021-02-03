'''
请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。
让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。
由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可

策略：打表+模拟
'''


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                         37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        pos_prime, ans = 0, 1
        for num in prime_numbers:
            if num <= n:
                pos_prime += 1
            else:
                break
        pos_num = n - pos_prime
        for i in range(2, pos_prime + 1):
            ans = (ans * i) % 1000000007
        for i in range(2, pos_num + 1):
            ans = (ans * i) % 1000000007
        return ans
