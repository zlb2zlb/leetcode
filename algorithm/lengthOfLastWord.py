#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 21:27
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : lengthOfLastWord.py
# @Software: PyCharm
## https://wiki.python.org/moin/TimeComplexity  内置函数的时间复杂度
## len() 函数
## split()函数

## 时间复杂度 O(n)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        length = len(words)
        for i in range(length-1,-1,-1):
            if words[i]:
                count_space = words[i].count(" ")
                count = 0
                for j in words[i]:
                    count += 1
                return count - count_space
        return 0
s = Solution()
print(s.lengthOfLastWord("hello world"))
print(s.lengthOfLastWord("      "))



## 学习
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        i = n-1
        while i >= 0:
            if s[i]==' ':
                continue
            else:
                break
        count = 0
        while i >= 0:
            if i == ' ':
                return count
            else:
                count += 1
        return count