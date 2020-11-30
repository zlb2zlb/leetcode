#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 9:24
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : minWindow.py
# @Software: PyCharm
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-window-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"

## 学习
import collections


def minWindow(self, s: str, t: str) -> str:
        need=collections.defaultdict(int)
        for c in t:
            need[c]+=1
        needCnt=len(t)
        i=0
        res=(0,float('inf'))
        for j,c in enumerate(s):
            if need[c]>0:
                needCnt-=1
            need[c]-=1
            if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
                while True:      #步骤二：增加i，排除多余元素
                    c=s[i]
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i<res[1]-res[0]:   #记录结果
                    res=(i,j)
                need[s[i]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt+=1
                i+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果


# 作者：Mcdull0921
# 链接：https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。