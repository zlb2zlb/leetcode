#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 8:50
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : minStack.py
# @Software: PyCharm

# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
#     push(x) —— 将元素 x 推入栈中。
#     pop() —— 删除栈顶的元素。
#     top() —— 获取栈顶元素。
#     getMin() —— 检索栈中的最小元素。

class Node:
    def __init__(self, x, min, next=None):
        self.val = x
        self.min = min
        self.next = next

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x: int) -> None:
        """
        因为栈是顺序插入的，因此每一个元素，ta的最小值只需要考虑从栈底到ta这一部分的即可，
        因此每次都用自身的值与当前最小值进行比较，min存储为当前元素所在部分最小值即可。
        :param x: 值
        :return:
        """
        if self.head == None:
            self.head = Node(x, x)
        else:
            self.head = Node(x, min(x,self.head.min), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()