#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 9:16
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : subsets.py
# @Software: PyCharm
from typing import List




class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = set(nums)
        lg = len(nums)
        if not lg:return []
        res = []
        res.append([])
        # 奇数情况下
        if lg%2 == 1:
            count = int(lg/2)
            for i in range(lg):
              pass

        # 偶数情况下
        if lg%2 == 0:
            pass
        return res

# 使用库函数
# https://docs.python.org/zh-cn/3.7/library/itertools.html#itertools.combinations
import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res


# 学习
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

nums = [1,2,3,4,5]
s = Solution()
print(s.subsets(nums))
# 作者：powcai
# 链接：https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。