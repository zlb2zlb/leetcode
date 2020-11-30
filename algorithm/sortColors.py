#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 9:20
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : sortColors.py
# @Software: PyCharm
from typing import List

## 时间复杂度O(n),空间复杂度O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in nums:
            if i == 0:
                count_0 += 1
            elif i == 1:
                count_1 += 1
            elif i == 2:
                count_2 += 1
        length = count_0 + count_1 + count_2
        for i in range(count_0):
            nums[i] = 0
        for i in range(count_0,count_0 + count_1):
            nums[i] = 1
        for i in range(count_0 + count_1,count_0 + count_1 + count_2):
            nums[i] = 2


## 学习，手撸快速排序，时间复杂度O(n),空间复杂度O(1)
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # all in [0, zero] = 0
        # all in (zero, i) = 1
        # all in (two, len - 1] = 2

        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        size = len(nums)
        if size < 2:
            return

        zero = -1
        two = size - 1

        i = 0

        while i <= two:
            if nums[i] == 0:
                zero += 1
                swap(nums, i, zero)
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(nums, i, two)
                two -= 1

# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/sort-colors/solution/kuai-su-pai-xu-partition-guo-cheng-she-ji-xun-huan/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
