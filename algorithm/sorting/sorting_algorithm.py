#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 9:02
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : sorting_algorithm.py
# @Software: PyCharm
from typing import List

import math

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

# 快速排序
'''
快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。
快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：

    从数列中挑出一个元素，称为 “基准”（pivot）；
    重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
    递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
'''
def quickSort(nums:List[int]) -> List[int]:
    '''
    时间复杂度：O(nlogn)  O(n*n)  O(nlogn)
    空间复杂度：O(nlogn)
    :param nums:无序数组
    :return:有序数组
    '''

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

    def sort(nums:List[int], low:int, high:int) -> None:
        if low < high:
            index = getIndex(nums, low, high)
            sort(nums, low, index - 1)
            sort(nums, index + 1, high)
    sort(nums, 0, len(nums)-1)
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
'''
a.将无需序列构建成一个堆，根据升序降序需求选择大顶堆或小顶堆;

　　b.将堆顶元素与末尾元素交换，将最大元素"沉"到数组末端;

　　c.重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，反复执行调整+交换步骤，直到整个序列有序。
'''
def heapSort(nums:List[int]) -> List[int]:
    '''
    不稳定
    时间复杂度：O(nlogn)  O(nlogn)  O(nlogn)
    空间复杂度：O(1)
    :param nums:无序数组
    :return:有序数组
    '''
    lg = len(nums)
    def sort(nums:List[int]):
        # 构建大顶堆
        for i in range(int(lg/2)-1,-1,-1):
            # 从第一个非叶子节点从下至上，从右至左调整结构
            adjustHeap(nums, i, lg)
        # 调整堆结构 + 交换堆顶元素与末尾元素
        for j in range(lg-1,0,-1):
            swap(nums, 0, j)
            adjustHeap(nums, 0, j)

    # 调整大顶堆
    def adjustHeap(nums:List[int], i:int, length:int):
        temp = nums[i] # 先取出当前元素
        k = i*2+1
        while k<lg:
            if (k+1<lg and nums[k]<nums[k+1]):# 如果左子节点小于右子节点，k指向右子节点
                k += 1
            if nums[k] > temp: # 如果子节点大于父节点，将子节点值赋给父节点（不用进行交换）
                nums[i] = nums[k]
                i = k
            else:
                break
            k = k*2+1

    def swap(nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp
    return nums

# 二路归并排序
'''
https://www.cnblogs.com/wuyepeng/p/9819827.html
二路归并排序主要运用了“分治算法”，分治算法就是将一个大的问题划分为n个规模较小而结构相似的子问题。

这些子问题解决的方法都是类似的，解决掉这些小的问题之后，归并子问题的结果，就得到了“大”问题的解。

　　二路归并排序主旨是“分解”与“归并”

　　分解：　　

　　　　1.将一个数组分成两个数组，分别对两个数组进行排序。

　　　　2.循环第一步，直到划分出来的“小数组”只包含一个元素，只有一个元素的数组默认为已经排好序。

　　归并：

　　　　1.将两个有序的数组合并到一个大的数组中。

　　　　2.从最小的只包含一个元素的数组开始两两合并。此时，合并好的数组也是有序的。
'''
def mergeSort(nums:List[int]) -> List[int]:
    '''
    稳定
    时间复杂度：O(nlogn)  O(nlogn)  O(nlogn)
    空间复杂度：O(n)
    :param nums:无序数组
    :return:有序数组
    '''
    low,high = 0,len(nums)-1
    def sort(low:int, high:int, nums:List[int]) -> List[int]:
        if low < high:
            mid = int((low + high)/2)
            sort(low, mid, nums)
            sort(mid+1, high, nums)
            merge(low, mid, high, nums)
    def merge(low:int, mid:int, high:int, nums:List[int]):
        i,j,p = low,mid+1,0
        res = [0]*(high-low+1)
        while i<=mid and j<=high:
            if nums[i]<=nums[j]:
                res[p] = nums[i]
                i += 1
            else:
                res[p] = nums[j]
                j += 1
            p += 1
        while i<=mid:
            res[p] = nums[i]
            i += 1
            p += 1
        while j<=high:
            res[p] = nums[j]
            j += 1
            p += 1
        p,i = 0,low
        while i <= high:
            nums[i] = res[p]
            p+=1
            i+=1
    sort(low, high, nums)
    return nums
# 多路归并排序

# 计数排序
'''
https://blog.csdn.net/csdnnews/article/details/83005778?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_baidulandingword-2&spm=1001.2101.3001.4242
'''
def countSort(nums:List[int]) -> nums:
    '''
    时间复杂度：O(n+k)  O(n+k)  O(n)
    空间复杂度：O(n+k)
    :param nums:无序数组
    :return:有序数组
    '''
    # 得到数列的最大值和最小值，并算出差值d
    maxNum = float('-inf')
    minNum = float('inf')
    for i in nums:
        if i > maxNum:
            maxNum = i
        elif i < minNum:
            minNum = i
    d = maxNum - minNum
    # 创建统计数组并统计对应元素个数
    countArray = [0] * (d + 1)
    for i in nums:
        countArray[i - minNum] += 1
    # 统计数组做变形，后面的元素等于前面的元素之和
    sum = 0
    for i in range(len(countArray)):
        sum += countArray[i]
        countArray[i] = sum
    # 倒序遍历原始数列，从统计数组找到正确位置，输出到结果数组
    sortedArray = [0]*len(nums)
    for i in range(len(nums)-1, -1, -1):
        sortedArray[countArray[nums[i]-minNum] - 1] = nums[i]
        countArray[nums[i]-minNum] -= 1

    return sortedArray

# 桶排序
'''
https://blog.csdn.net/qq_27124771/article/details/87651495
划分多个范围相同的区间，每个子区间自排序，最后合并。
'''
def bucketSort(nums:List[int]) -> List[int]:
    '''
    时间复杂度：O(n+k)  O(n*n)  O(n)
    空间复杂度：O(n+k)
    :param nums:无序数组
    :return:有序数组
    '''
    lg = len(nums)
    sortedArr = [0]*lg
    # 计算最大值与最小值
    maxNum = float('-inf')
    minNum = float('inf')
    for i in nums:
        maxNum = max(i, maxNum)
        minNum = min(i, minNum)

    # 计算桶的数量
    bucketNum = int((maxNum - minNum) / lg) + 1
    bucketArr = []
    for i in range(bucketNum):
        bucketArr.append([])

    # 将每个元素放入桶
    for i in range(lg):
        num = int((nums[i] - minNum) / lg)
        bucketArr[num].append(nums[i])

    # 对每个桶进行排序
    for i in range(len(bucketArr)):
        bucketArr[i].sort()

    # 将桶中的元素赋值到原序列
    index = 0
    for i in range(len(bucketArr)):
        for j in range(len(bucketArr[i])):
            sortedArr[index] = bucketArr[i][j]
            index += 1
    return sortedArr


# 基数排序

if __name__ == '__main__':
    nums1 = nums.copy()
    sorted_nums = bubbleSort(nums1)
    print(sorted_nums)
    # sorted_nums = selectionSort(nums)
    # print(sorted_nums)
    # sorted_nums = insertionSort(nums)
    # print(sorted_nums)
    # sorted_nums = quickSort(nums)
    # print(sorted_nums)
    # sorted_nums = countSort(nums)
    # print(sorted_nums)
    # sorted_nums = bucketSort(nums)
    # print(sorted_nums)
    # sorted_nums = bucketSort(nums)
    # print(sorted_nums)
    sorted_nums = mergeSort(nums)
    print(sorted_nums)
