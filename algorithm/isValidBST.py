#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 9:16
# @Author  : zlb
# @Email   : 15967924690@163.com
# @File    : isValidBST.py
# @Software: PyCharm
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
#     节点的左子树只包含小于当前节点的数。
#     节点的右子树只包含大于当前节点的数。
#     所有左子树和右子树自身必须也是二叉搜索树。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/validate-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.

## 提取共性规律，递归解决问题
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.recursion(root,float('-inf'),float('inf'))
    def recursion(self,root,min_val,max_val):
        ## 空节点返回True
        if root == None:return True

        ##  节点值超出范围返回 False
        if root.val <= min_val or root.val >= max_val:return False

        if self.recursion(root.left,min_val,root.val) == False:return False
        if self.recursion(root.right,root.val,max_val) == False:return False
        return True

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
s = Solution()
print(s.isValidBST(tree))