#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 21:22
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : mergeIntervals.py
# @Software: PyCharm

# 给出一个区间的集合，请合并所有重叠的区间
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-intervals
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:return []
        ## 删除无效数据
        for x in intervals:
            if x == []:
                intervals.remove(x)
        ## 排序列表
        intervals_sorted = sorted(intervals,key=lambda x:x[0])
        i,j = 0,0
        while i < len(intervals_sorted):
            j = i + 1
            while j < len(intervals_sorted):
                if intervals_sorted[i][1] >= intervals_sorted[j][0]:
                    if intervals_sorted[i][1] > intervals_sorted[j][1]:
                        pass
                    else:
                        intervals_sorted[i][1] = intervals_sorted[j][1]
                    del intervals_sorted[j]
                else:
                    j += 1
            i += 1
        return intervals_sorted
