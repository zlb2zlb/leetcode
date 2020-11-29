#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 10:37
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : search.py
# @Software: PyCharm
# 给你一个整数数组 nums ，和一个整数 target 。
# 该整数数组原本是按升序排列，但输入时在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。
# 请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 时间复杂度 O(n)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 0:return -1
        if length == 1:return 0 if nums[0] == target else -1
        ## 当往小了找，却找到更大的数值时，结束
        i = 0
        if nums[i] > target:
            while nums[i] > target:
                if nums[i - 1] > nums[i]:
                    return -1
                i -= 1
        elif nums[i] < target:
            while nums[i] < target and i < length-1:
                if nums[i + 1] < nums[i]:
                    return -1
                i += 1
        if nums[i] == target:
            return length + i if i < 0 else i
        ## 当往大了找，却找到更小的数值时，结束
        return -1

nums = [4,5,6,7,0,1,2]
target = 3
# nums = [4,5,6,7,0,1,2]
# target = 0
# nums = [1]
# target = 1
nums = [1,3]
target = 3
s = Solution()
print(s.search(nums,target))