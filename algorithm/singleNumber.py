#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 10:55
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : singleNumber.py
# @Software: PyCharm
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:return nums[0]
        while nums:
            i = nums[0]
            nums.remove(i)
            if i in nums:
                nums.remove(i)
                continue
            else:
                return i

s = Solution()
print(s.singleNumber([2,2,1]))

# 设存在数字a, b, c：
#
#     a ^ a = 0
#     a ^ 0 = a
#     a ^ b ^ c = a ^ c ^ b
#
# 初始化res为0，将所有数字异或，相同的数字将被消除，最终res就是仅出现1次的数字和0的异或，即结果。
#
# 作者：jue-qiang-zha-zha
# 链接：https://leetcode-cn.com/problems/single-number/solution/136-zhi-chu-xian-yi-ci-de-shu-zi-yi-huo-kv3nh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0
        for num in nums:
            s = s ^ num

        return s

