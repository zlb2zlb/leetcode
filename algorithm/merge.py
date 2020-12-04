#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 9:42
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : merge.py
# @Software: PyCharm
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 输入：
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出：[1,2,2,3,5,6]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# ums1、nums2的长度已知，但nums1给出的数组为[1,2,3,0,0,0]，后面的0代表nums2的长度。
# 因为是有序数组，所以我们可以从后往前填入，[...,0,0,0]开始填入。
#
#     i = m-1,j = n-1, k = m+n-1
#     选取 max(nums1[i]、nums2[j]) 填入 nums1[k] 同时，k、i/j往前移动一个。
#     因为是在nums1上操作，所以需要考虑当i==-1时，将nums2的所有数组元素赋值给nums1即可
#
# 作者：hungry-7ederberg
# 链接：https://leetcode-cn.com/problems/merge-sorted-array/solution/bu-lou-by-hungry-7ederberg-7l0t/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # lg1 = len(nums1)
        # lg2 = len(nums2)
        # for i in range(lg2):
        #     nums1.append(0)
        #
        # i, j, k = lg1-1, lg2-1, lg1+lg2-1
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return
        i, j, k = m-1, n-1, m+n-1
        while j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
                if i == -1:
                    nums1[0:j+1] = nums2[0:j+1]
                    return
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1



# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
# s = Solution()
# s.merge(nums1, 3, nums2, 3)
# print(nums1)
#
# nums1 = [0]
# nums2 = [1]
# s = Solution()
# s.merge(nums1, 0, nums2, 1)
# print(nums1)
#
# nums1 = [0]
# nums2 = []
# s = Solution()
# s.merge(nums1, 1, nums2, 0)
# print(nums1)
#
#
# nums1 = [2,0]
# m = 1
# nums2 = [1]
# n = 1
# s = Solution()
# s.merge(nums1, m, nums2, n)
# print(nums1)

nums1 = [0,0,0,0,0]
m = 0
nums2 = [1,2,3,4,5]
n = 5
s = Solution()
s.merge(nums1, m, nums2, n)
print(nums1)


# 思路一致，代码简洁，学习！！

# 标签：从后向前数组遍历
# 因为 nums1 的空间都集中在后面，所以从后向前处理排序的数据会更好，节省空间，一边遍历一边将值填充进去
# 设置指针 len1 和 len2 分别指向 nums1 和 nums2 的有数字尾部，从尾部值开始比较遍历，同时设置指针 len 指向 nums1 的最末尾，每次遍历比较值大小之后，则进行填充
# 当 len1<0 时遍历结束，此时 nums2 中海油数据未拷贝完全，将其直接拷贝到 nums1 的前面，最后得到结果数组
# 时间复杂度：O(m+n)O(m+n)O(m+n)
#
# 作者：guanpengchn
# 链接：https://leetcode-cn.com/problems/merge-sorted-array/solution/hua-jie-suan-fa-88-he-bing-liang-ge-you-xu-shu-zu-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。