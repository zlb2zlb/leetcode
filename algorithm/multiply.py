#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 8:19
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : multiply.py
# @Software: PyCharm
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
#
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/multiply-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numDict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        l1 = list(num1)
        l2 = list(num2)
        n1 = 0
        n2 = 0
        bit1 = len(num1) - 1
        bit2 = len(num2) - 1
        for i in l1:
            for key in numDict.keys():
                if i == key:
                    n1 += numDict[key] * 10**bit1
                    bit1 -= 1
        for j in l2:
            for key in numDict.keys():
                if j == key:
                    n2 += numDict[key] * 10**bit2
                    bit2 -= 1
        return str(n1*n2)

# 作者：yi-wen-statistics
# 链接：https://leetcode-cn.com/problems/multiply-strings/solution/bao-li-qiu-jie-by-yi-wen-statistics-5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

num1 = "10"
num2 = "12"
num1 = "123"
num2 = "456"
s = Solution()
num = s.multiply(num1, num2)
print(num)
