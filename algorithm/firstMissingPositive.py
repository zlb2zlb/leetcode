#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 8:16
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : firstMissingPositive.py
# @Software: PyCharm

# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
# 输入: [7,8,9,11,12]
# 输出: 1
#
# 输入: [3,4,-1,1]
# 输出: 2
# 输入: [1,2,0]
# 输出: 3
from typing import List

## 使用了 sorted 排序，时间复杂度为 O(n),空间复杂度为 O(n)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums == []:return 1
        nums.append(0)
        nums = sorted(nums)
        index_0 = nums.index(0)
        num,i,length = 1,index_0,len(nums)
        while i < length:
            if num == nums[i]:
                num += 1
            elif num < nums[i]:
                return num
            i += 1
        return num



s = Solution()
# nums = [7,8,9,11,12]
# nums = [3,4,-1,1]
nums = [1,2,0]
nums = [-1,-2,-3]
re = s.firstMissingPositive(nums)
print(re)

## 学习,时间复杂度 O(n),空间复杂度O(1),桶排序
## 数组位置对应数字，每个数字回到自己对应的位置上，a[i-1] = i
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i,a in enumerate(nums): #所有负数和超过numsSize的数（没票的人）都置为0（赶走）。
            if not(0<=a<=len(nums)): nums[i]=0
        for i,a in enumerate(nums):
            if 0==a or a==i+1:continue  #跳过空座位，检查座位没坐对的
            nums[i]=0   # a错坐nums[i]了，要起来找正确座位，原nums[i]置零表示空余
            while(a!=nums[a-1]):  #循环直到a坐对位置nums[a-1]
                if(0==nums[a-1]):   #是空余位置，直接覆盖
                    nums[a-1]=a
                else:              #有“人”在此，让TA离开，a坐上。
                    nums[a - 1],a = a ,nums[a-1] #TA相当于新的a，去找自己的座位
        try: return 1+nums.index(0) #找到首个空位置nums[i]==0，则i+1号乘客缺席
        except: return 1+len(nums)  #满座，返回N+1


# 作者：java_Lee
# 链接：https://leetcode-cn.com/problems/first-missing-positive/solution/zhao-zuo-wei-de-gu-shi-onyuan-di-jie-fa-by-java_le/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
s = Solution()
nums = [7,8,9,11,12]
nums = [3,4,-1,1]
nums = [1,2,0]
# nums = [-1,-2,-3]
re = s.firstMissingPositive(nums)
print(re)


