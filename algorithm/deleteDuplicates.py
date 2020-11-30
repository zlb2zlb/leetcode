#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 20:24
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : deleteDuplicates.py
# @Software: PyCharm

# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
## 因为是排序列表，所以重复元素必定是相邻的，因此双指针可解决
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ## 空链表，只有一个元素的链表
        class Solution:
            def deleteDuplicates(self, head: ListNode) -> ListNode:
                if head == None or head.next == None: return head
                l = head
                r = head.next
                while r:
                    if l.val == r.val:
                        l.next = r.next
                    else:
                        l = r
                    r = r.next
                return head
s = Solution()
lists = [0,1,1,1,2,3,3]
head = ListNode(0)
p = head
for val in lists:
    p.next = ListNode(val)
    p = p.next
head_ = s.deleteDuplicates(head)
while head_:
    print(head_.val)
    head_ = head_.next