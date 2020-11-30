#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/28 13:46
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : hasCycle.py
# @Software: PyCharm

# 给定一个链表，判断链表中是否有环。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 如果链表中存在环，则返回 true 。 否则，返回 false 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/linked-list-cycle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

## 特殊值，或者动态添加一个属性值（python）（空间复杂度O(1)，变更原链表数值）
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:return False
        p = head
        while p.next:
            p.val = float("-inf")
            if p.next.val == float("-inf"):
                return True
            p = p.next
        return False

## 学习！
## 使用hash表记录已经访问过的节点
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 1. python map  dict.get(key,default=None)，如果字典中没有，则默认返回None
        m = {}
        while head:
            if m.get(head):
                return True
            m[head] = 1
            head = head.next
        return False

# 快慢指针（龟兔赛跑，空间复杂度O(1)）
# 枚举时添加一个慢一拍的指针，如果有环最终两个指针会相遇
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 2. slow fast point
        sp, fp, si = head, head, False
        while fp:
            if si:
                sp = sp.next
                si = False
            else:
                si = True
            fp = fp.next
            if sp == fp:
                return True
        return False

# 作者：ydykid
# 链接：https://leetcode-cn.com/problems/linked-list-cycle/solution/wu-chong-jie-ti-si-lu-ji-lu-hashbiao-kuai-man-zhi-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。