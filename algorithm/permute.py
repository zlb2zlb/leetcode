#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 8:34
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : permute.py
# @Software: PyCharm
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# 长度为 n 的数组nums，排列结果 res 等于在长度为 n-1 的数组所得排列结果的每个List中，依次在(0,n-1)位置上加入 nums[n-1]
# 使用递归完成计算
import itertools


# 长度为 n 的数组nums，排列结果 res 等于在长度为 n-1 的数组所得排列结果的每个List中，依次在(0,n-1)位置上加入 nums[n-1]
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1 or n == 0:return [nums]
        res = self.fun(nums[0:-1], nums[-1])
        res.sort(key=lambda x: (x[0]))
        return res

    def fun(self, nums:List[int], num:int) -> List[List[int]]:
        if len(nums) == 1:return [[nums[0],num],[num,nums[0]]]
        else:
            res = self.fun(nums[0:-1], nums[-1])
        length_res = len(res)
        for i in range(length_res):
            length = len(res[0])
            for j in range(length + 1):
                temp = res[0].copy()
                temp.insert(j, num)
                res.append(temp)
            del res[0]
        return res



nums = [1, 2, 3, 4]
print(nums[0:-1], nums[-1])
s = Solution()
res = s.permute(nums)
for r in res:
    print(r)


# 执行时间最短
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [];
        def findx(currentIndex):
            if currentIndex == len(nums)-1:
                # locaList = nums.copy();
                res.append(nums.copy());
            for i in range(currentIndex,len(nums)):
                nums[i],nums[currentIndex] = nums[currentIndex],nums[i];
                findx(currentIndex+1);
                nums[i],nums[currentIndex] = nums[currentIndex],nums[i];

        findx(0);
        return res;


# 执行内存最少，和我的方式差不多，代码上更简洁
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res_1 = self.permute(nums[:-1])
        res = []
        cur_num = nums[-1]
        for re in res_1:
            for i in range(len(nums)):
                tmp_res = re.copy()
                tmp_res.insert(i,cur_num)
                res.append(tmp_res)
        return res

# 调用库函数
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
nums = [1, 2, 3, 4]
print(nums[0:-1], nums[-1])
s = Solution()
res = s.permute(nums)
for r in res:
    print(r)



