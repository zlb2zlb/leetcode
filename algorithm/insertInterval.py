#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 8:06
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : insertInterval.py
# @Software: PyCharm
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if newInterval == []:return intervals
        if intervals == []:return [newInterval]
        intervals.append(newInterval)
        intervals_0 = sorted(intervals, key=lambda x: x[0])
        intervals_1 = sorted(intervals, key=lambda x: x[1])
        start = intervals_0.index(newInterval) ## 确定区间开头位置
        stop = intervals_1.index(newInterval) ##  确定区间结束位置
        if start < stop:
            ## 两者位置不同，说明横跨了几个区间，将这区间合并
            for i in range(start + 1, stop + 1):
                del intervals_0[start + 1]
        elif start > stop:
            del intervals_0[start]
            return intervals_0

        ## newInterval的开头与结尾分别与前后区间的大、小值进行比较，确定是否需要合并前后两个区间
        if start < len(intervals_0)-1 and intervals_0[start][1] >= intervals_0[start + 1][0]:
                intervals_0[start][1] = intervals_0[start + 1][1]
                del intervals_0[start + 1]
        if start > 0 and intervals_0[start][0] <= intervals_0[start - 1][1]:
                intervals_0[start][0] = intervals_0[start - 1][0]
                del intervals_0[start - 1]
        return intervals_0

intervals = [[1,3],[6,9]]
newInterval = [2,5]
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
# intervals = []
# newInterval = [4,8]
# intervals = [[1,5]]
# newInterval = [2,3]
# intervals = [[1,5],[6,8]]
# newInterval = [0,9]
s = Solution()
intervals = s.insert(intervals,newInterval=newInterval)
print(intervals)

## 消耗时间最短
## 下面这个思路简单明了，学习学习
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        re = []
        left = newInterval[0]
        right = newInterval[1]
        flag = 0 ## 标志是否已结束寻找
        for interval in intervals:
            if flag ==1:
                re.append(interval)
                continue
            if interval[1]<left:
                re.append(interval)
                continue
            if interval[0]>right:## 遇到下一个区间左值大于right时，代表已经结束，此时将区间放入列表中，并设置flag=1
                re.append([left,right])
                flag = 1
                re.append(interval)
                continue
            left = min(left,interval[0])
            right = max (right,interval[1])
        if flag ==0:
            re.append([left,right])
        return re


## 消耗内存最少
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = 0
        while i<n:
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif  newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
                i+=1
            else:
                left = min(intervals[i][0],newInterval[0])
                right = max(intervals[i][1],newInterval[1])
                while i<n-1 and intervals[i+1][0]<=right:
                    i+=1
                    right = max(right,intervals[i][1])
                res.append([left,right])
                return res + intervals[i+1:]
        return res+[newInterval]



