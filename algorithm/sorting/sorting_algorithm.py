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
    空间复杂度：O(1)
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

'''
快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。
快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：

    从数列中挑出一个元素，称为 “基准”（pivot）；
    重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
    递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
'''
# 快速排序
def quickSort(nums:List[int]) -> List[int]:
    '''
    时间复杂度：O(nlogn)  O(n*n)  O(nlogn)
    空间复杂度：O(nlogn)
    :param nums:无序数组
    :return:有序数组
    '''
    def sort(nums:List[int], low:int, high:int) -> None:
        if low < high:
            index = getIndex(nums, low, high)
            sort(nums, low, index - 1)
            sort(nums, index + 1, high)
    def getIndex(nums:List[int], low:int, high:int):
        temp = nums[low]
        while (low < high):
            # 从队尾往前移动，直到遇到第一个小于基准值停下
            while (low < high and nums[high]>=temp):
                high -= 1
            # 如果队尾元素小于temp了, 需要将其赋值给low
            nums[low] = nums[high]
            # 从队首往后移动，直到遇到第一个大于基准值停下
            while (low < high and nums[low] <= temp):
                low += 1
            # 如果队首元素大于temp了, 需要将其赋值给high
            nums[high] = nums[low]
        # 跳出循环时low和high相等, 此时的low或high就是temp的正确索引位置
        # 由原理部分可以很清楚的知道low位置的值并不是temp, 所以需要将temp赋值给arr[low]
        nums[low] = temp
        return low # 返回temp的正确位置

    return nums

# 简单插入排序
'''
插入排序（Insertion-Sort）的算法描述是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：

    从第一个元素开始，该元素可以认为已经被排序；
    取出下一个元素，在已经排序的元素序列中从后向前扫描；
    如果该元素（已排序）大于新元素，将该元素移到下一位置；
    重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
    将新元素插入到该位置后；
    重复步骤2~5。
'''
def insertionSort(nums:List[int]) -> List[int]:
    '''
    时间复杂度：O(n*n)  O(n*n)  O(n)
    空间复杂度O：(1)
    :param nums:无序数组
    :return:有序数组
    '''
    for i in range(len(nums) - 1):
        j = i + 1
        temp = nums[j]
        while temp < nums[j - 1] and j > 0:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = temp

    return nums

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
    空间复杂度：O(1)
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
    sorted_nums = insertionSort(nums)
    print(sorted_nums)
    sorted_nums = quickSort(nums)
    print(sorted_nums)
