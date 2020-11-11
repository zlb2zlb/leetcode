#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 21:27
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : mergeLists.py
# @Software: PyCharm

# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists)==0:return
        head = ListNode(None)
        head.next = lists[0]
        for l in lists[1:]:
            result_head = ListNode(None)
            result_head.next = self.mergeTwoLists(head.next,l)
            head = result_head
        return head.next
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        p = head
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                p = p.next
                l1 = l1.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next
        if not l1:
            p.next = l2
        else:
            p.next = l1
        return head.next

s = Solution()
lists = [[],[1,4,5],[1,3,4],[0,2,6]]
lists_node = []
for l in lists:
    head = ListNode(None)
    p = head
    for val in l:
        head.next = ListNode(val)
        head = head.next
    lists_node.append(p.next)
for p in lists_node:
    while p != None:
        print(p.val)
        p = p.next
p = s.mergeKLists(lists_node)
p = p.next
while p != None:
    print(p.val)
    p = p.next