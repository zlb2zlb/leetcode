#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 9:15
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : maxDepth.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left_high = self.maxDepth(root.left)
        right_high = self.maxDepth(root.right)

        return max(left_high, right_high) + 1

# 树生成代码   https://blog.csdn.net/baoxin1100/article/details/108025393
def generate_tree(vals):
    if len(vals) == 0:
        return None
    que = [] # 定义队列
    fill_left = True # 由于无法通过是否为 None 来判断该节点的左儿子是否可以填充，用一个记号判断是否需要填充左节点
    for val in vals:
        node = TreeNode(val) if val else None # 非空值返回节点类，否则返回 None
        if len(que)==0:
            root = node # 队列为空的话，用 root 记录根结点，用来返回
            que.append(node)
        elif fill_left:
            que[0].left = node
            fill_left = False # 填充过左儿子后，改变记号状态
            if node: # 非 None 值才进入队列
                que.append(node)
        else:
            que[0].right = node
            if node:
                que.append(node)
            que.pop(0) # 填充完右儿子，弹出节点
            fill_left = True #
    return root

null = None
vals = [3,1,20,null,null,15,25]
tree = generate_tree(vals)


root = TreeNode()
s = Solution()
print(s.maxDepth(tree))