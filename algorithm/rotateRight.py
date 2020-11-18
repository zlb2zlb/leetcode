#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 8:49
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : rotateRight.py
# @Software: PyCharm

# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotate-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 时间复杂度为 O(n),空间复杂度为 O(1)
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 遍历链表，求出链表长度length与k取余
        # 并将头尾连接起来形成环形链
        if not head or k==0:return head
        length = 1
        p = head
        ## 计算length 形成环形链
        while p.next:
            length += 1
            p = p.next
        p.next = head
        ## head移动，并找到断开点
        count = length - k % length
        p = head
        for i in range(count-1):
            p = p.next
        head = p.next
        p.next = None
        return head


lists = [0,1,1,1,2,3,3]
# lists = [0]
head = ListNode(None)
p = head
for val in lists:
    p.next = ListNode(val)
    p = p.next
s = Solution()
k = 3
head_ = s.rotateRight(head.next,k)
while head_:
    print(head_.val)
    head_ = head_.next