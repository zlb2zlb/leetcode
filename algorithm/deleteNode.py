#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/28 12:54
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : deleteNode.py
# @Software: PyCharm
# Definition for singly-linked list.
# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。
# 一般来说，我们要删除一个节点，会传入一个链表和一个节点值，但本题中并没有传入这两个参数，而是传入了一个结构体，节点
# 即我们需要直接对这个节点进行操作，将该节点删除！前一个节点连接到后一个节点上
# 但是！！单向链表，只能对后续节点操作，因此，需要将 node.next.val 赋给 node.val ，并将 node.next 连接到 node.next.next 上
# 也就是，删除了当前节点的后一个节点！


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


head = ListNode(None)
p = head
nodes = [1,2,3,4,5,6]
for node in nodes:
    p.next = ListNode(node)
    p = p.next

s = Solution()
s.deleteNode(head.next.next.next)

p = head.next
while p:
    print(p.val)
    p = p.next


## 学习学习！！https://leetcode-cn.com/problems/delete-node-in-a-linked-list/solution/zhe-shi-yi-ge-kong-bu-ti-a-tai-ke-pa-liao-leetcode/
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution:
        def deleteNode(self, node):
            """
            :type node: ListNode
            :rtype: void Do not return anything, modify node in-place instead.
            """
            node.val = node.next.val
            node.next = node.next.next


# 作者：kou - zi - 6
# 链接：https: // leetcode - cn.com / problems / delete - node - in -a - linked - list / solution / zhe - shi - yi - ge - kong - bu - ti - a - tai - ke - pa - liao - leetcode /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。