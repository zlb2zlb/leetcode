#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 9:14
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : maxSubArray.py
# @Software: PyCharm
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
from typing import List

# 这道题用动态规划的思路并不难解决，比较难的是后文提出的用分治法求解，但由于其不是最优解法，所以先不列出来
# 动态规划的是首先对数组进行遍历，当前最大连续子序列和为 sum，结果为 ans
# 如果 sum > 0，则说明 sum 对结果有增益效果，则 sum 保留并加上当前遍历数字
# 如果 sum <= 0，则说明 sum 对结果无增益效果，需要舍弃，则 sum 直接更新为当前遍历数字
# 每次比较 sum 和 ans的大小，将最大值置为ans，遍历结束返回结果
# 时间复杂度：O(n)O(n)O(n)
#
# 作者：guanpengchn
# 链接：https://leetcode-cn.com/problems/maximum-subarray/solution/hua-jie-suan-fa-53-zui-da-zi-xu-he-by-guanpengchn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 思路一致，但是没能实现出来！代码能力需要加强，下列实现部分为学习上述作者

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = -2**32
#         length = len(nums)
#         i, j = 0, 1
#         flag = True
#         while flag:
#             while j < length:
#                 tmp = sum(nums[i:j])
#                 max_sum = max_sum if max_sum > tmp else tmp
#                 count = 1
#                 if nums[j] > 0:
#                     while nums[i] < 0:
#                         i += 1
#                     while sum(nums[i:i+count]) < 0:
#                         count += 1
#                     i += count
#                 j += 1
#             while i<j:
#                 count = 0
#                 tmp = sum(nums[i:j])
#                 while nums[i] < 0:
#                     i += 1
#                 while sum(nums[i:i + count]) < 0:
#                     count += 1
#                 i += count
#                 max_sum = max_sum if max_sum > tmp else tmp
#                 flag = False
#
#         return max_sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -2**32
        sum_array = -2**32
        for num in nums:
            if sum_array > 0:
                sum_array += num
            else:
                sum_array = num
            max_sum = max(max_sum, sum_array)
        return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSubArray(nums))