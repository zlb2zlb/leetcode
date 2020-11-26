#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 10:55
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : climbStairs.py
# @Software: PyCharm
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。
# 示例 1：
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/climbing-stairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 写出前6个数字的值，根据观察得到 这数字规律和 斐波那契数列 一样。因此直接做一个斐波那契数列的值
## 但是超时了。。。。。。。。。。
## 上一个斐波那契的计算公式，直接出来了
import time
class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        if n > 2:
            count = count + self.climbStairs(n - 1) + self.climbStairs(n - 2)
        if n == 2:return 2
        if n == 1:return 1
        return count
t_start = time.time()
s = Solution()
print(s.climbStairs(38))
t_stop = time.time()
print(t_stop - t_start)

## 这个解释很不错，学习
##标签：动态规划
# 本问题其实常规解法可以分成多个子问题，爬第n阶楼梯的方法数量，等于 2 部分之和
#
#     爬上 n−1n-1n−1 阶楼梯的方法数量。因为再爬1阶就能到第n阶
#     爬上 n−2n-2n−2 阶楼梯的方法数量，因为再爬2阶就能到第n阶
#
# 所以我们得到公式 dp[n]=dp[n−1]+dp[n−2]dp[n] = dp[n-1] + dp[n-2]dp[n]=dp[n−1]+dp[n−2]
# 同时需要初始化 dp[0]=1dp[0]=1dp[0]=1 和 dp[1]=1dp[1]=1dp[1]=1
# 时间复杂度：O(n)O(n)O(n)
#
# 作者：guanpengchn
# 链接：https://leetcode-cn.com/problems/climbing-stairs/solution/hua-jie-suan-fa-70-pa-lou-ti-by-guanpengchn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# 直接斐波那契数列的计算公式
class Solution:
    def climbStairs(self, n: int) -> int:
        import math
        sqrt5=5**0.5
        fibin=math.pow((1+sqrt5)/2,n+1)-math.pow((1-sqrt5)/2,n+1)
        return int(fibin/sqrt5)
t_start = time.time()
s = Solution()
print(s.climbStairs(38))
t_stop = time.time()
print(t_stop - t_start)
# 作者：821218213
# 链接：https://leetcode-cn.com/problems/climbing-stairs/solution/70zhong-quan-chu-ji-python3hui-ji-liao-ti-jie-qu-w/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。