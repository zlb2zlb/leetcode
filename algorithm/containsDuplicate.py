#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/28 12:37
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : containsDuplicate.py
# @Software: PyCharm
# 给定一个整数数组，判断是否存在重复元素。
# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

from typing import List

## 排序之后，两两对比。时间复杂度 O(nlogn),空间复杂度 O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 0 or length == 1:return False
        nums.sort()
        for i in range(length - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

s = Solution()
nums = [1,2,3,1]
nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]
print(s.containsDuplicate(nums))

## 学习
## 执行用时少。时间复杂度 O(len(t)),t为重复数字的个数。set()的时间复杂度小。
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setRes = set(nums)
        return len(nums ) != len(setRes)