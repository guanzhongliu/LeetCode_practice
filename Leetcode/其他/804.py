'''
国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串
比如: "a" 对应 ".-", "b" 对应 "-...", "c" 对应 "-.-.", 等等。

'''
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        temp = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        t = set()
        for word in words:
            res = ''
            for i in word:
                res += temp[ord(i) - 97]
            t.add(res)
        
        return len(t)


words = ["gin", "zen", "gig", "msg"]
solution = Solution()
print(solution.uniqueMorseRepresentations(words))