#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/12/5 14:57
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : uniquePaths.py
# @Software: PyCharm

# 从后往前去推。
# 到达end（x,y）有(x-1,y),(x,y-1)两种情况，x>0,y>0
# 当x=0时，只有(x,y-1)的可能，直到y=0。（x,y 反之亦然）
# 使用这个递归的方法能实现，但是会出现超时的现象，因为会在同一个节点上重复求解（几种方式经过，就会重复多少次）
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dg(x, y):
            if x == 1 or y == 1:return 1
            else:
                return dg(x-1, y) + dg(x,y-1)
        x, y = m, n
        res = dg(x, y)
        return res
s = Solution()
print(s.uniquePaths(3,2))
print(s.uniquePaths(4,3))
print(s.uniquePaths(7,4))
print(s.uniquePaths(23,12))

# 动态规划，状态压缩，如上面所说，每一次(x, y)的状态只与(x-1, y)/(x, y-1)相关
# 因此可以写一个矩阵，每个位置的状态（次数）直接写在上面，这样的话，就可以直接相加次数，省去重复的部分
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        state = [[0]*n for row in range(m)]
        for i in range(m):
            state[i][0] = 1
        for i in range(n):
            state[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                state[i][j] = state[i-1][j] + state[i][j-1]
        return state[m-1][n-1]
s = Solution()
print(s.uniquePaths(3,2))
print(s.uniquePaths(4,3))
print(s.uniquePaths(7,4))
print(s.uniquePaths(23,12))

# 解题思路
#
# 动态规划5大步骤：
#
# 1.定义状态：即定义数据元素的含义，这里定义dp[i][j]为当前位置的路径数，i表示i列，j表示j行
#
# 2.建立状态转移方程：因为从题目要求中可以看出，机器人只能向右或向下移动。所以到达dp[i][j]就可能是经过dp[i-1][j]到达，
# 也可能是经过dp[i][j-1]到达。所以状态转移方程为：dp[i][j]=dp[i-1][j]+dp[i][j-1]
#
# 3.设定初始值：通过状态转移方程可以看出，i和j下表要从1开始，否则会导致数组溢出异常。同时每一个位置点代表到达当前位置的路径条数，所以要设置最初的路径条数即dp[i][0]=1,dp[0][j]=1，即第一行，第一列值为1。
#
# 5.状态压缩：即优化数组空间，每次状态的更新只依赖于前一次的状态，优化一般作用于多维数组，观察是否可以将多维数组以一维数组来动态表示，即用一维数组来保存上次的状态。这道题的优化方法是存在的。具体看下面的代码解释。状态转移方程：dp[i] = dp[i-1] + dp[i]
#
# 6.选出结果：根据状态转移方程，求路径的总数，因此dp[-1][-1]表示的是到达最后位置的路径总条数。
#
# 作者：yu-fa-tang-you-dian-tian
# 链接：https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-ya-suo-shu-zu-you-hua-kong-jian-f/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。