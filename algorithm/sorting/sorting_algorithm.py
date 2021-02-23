#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 9:02
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : sorting_algorithm.py
# @Software: PyCharm
from typing import List

nums = [3,5,8,35,21,1,9,4,5,8,2,33,64,85,12,4,5,95]

## 比较算法

# 冒泡排序
'''
    # 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
    # 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
    # 针对所有的元素重复以上的步骤，除了最后一个；
    # 重复步骤1~3，直到排序完成。
'''
def bubbleSort(nums:List[int]) -> List[int]:
    '''
    时间复杂度：O(n*n)  O(n*n)  O(n)
    空间复杂度O：(1)
    :param nums:无序数组
    :return:有序数组
    '''
    for i in range(len(nums)):
        for j in range(len(nums) -1 - i):
            if nums[j] > nums[j+1]:
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp
    return nums

# 快速排序

# 简单插入排序

# 希尔排序

# 选择排序
'''
选择排序(Selection-sort)是一种简单直观的排序算法。
它的工作原理：
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。 

n个记录的直接选择排序可经过n-1趟直接选择排序得到有序结果。具体算法描述如下：

    初始状态：无序区为R[1..n]，有序区为空；
    第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
    n-1趟结束，数组有序化了。

'''
def selectionSort(nums:List[int]) -> List[int]:
    '''
    时间复杂度：O(n*n)  O(n*n)  O(n*n)
    空间复杂度O：(1)
    :param nums:无序数组
    :return:有序数组
    '''
    for i in range(len(nums) - 1):
        minIndex = i
        for j in range(i + 1, len(nums)):
            if nums[minIndex] > nums[j]:
                minIndex = j
        temp = nums[i]
        nums[i] = nums[minIndex]
        nums[minIndex] = temp
    return nums

# 堆排序

# 二路归并排序

# 多路归并排序

# 计数排序

# 桶排序

# 基数排序

if __name__ == '__main__':
    sorted_nums = bubbleSort(nums)
    print(sorted_nums)
    sorted_nums = selectionSort(nums)
    print(sorted_nums)
