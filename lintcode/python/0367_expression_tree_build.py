#!/usr/bin/python -t

# lintcode 370
# https://www.lintcode.com/problem/convert-expression-to-reverse-polish-notation/solution?_from=ladder&&fromId=106
# 根据运算符的优先级来构造单调递增栈，最后弹出栈中元素，最后一个就是根节点，返回即可。

"""
Definition of ExpressionTreeNode:
class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: expression: A string array
    @return: The root of expression tree
    """
    def build(self, expression):
        # write your code here
        if not expression:
            return None
        #two stacks
        nums = []
        ops = []
        for item in expression:
            if item.isdigit():
                nums.append(ExpressionTreeNode(item))
            elif item == '(':
                ops.append(ExpressionTreeNode(item))
            elif item in ["+", "-"]:
                while ops and ops[-1].symbol != '(':
                    operation = ops.pop()
                    operation.right = nums.pop()
                    operation.left = nums.pop()
                    nums.append(operation)
                ops.append(ExpressionTreeNode(item))
            elif item in ["/", "*"]:
                while ops and ops[-1].symbol in ["/", "*"]:
                    operation = ops.pop()
                    operation.right = nums.pop()
                    operation.left = nums.pop()
                    nums.append(operation)
                ops.append(ExpressionTreeNode(item))
            else: 
                while ops and ops[-1].symbol != '(':
                    operation = ops.pop()
                    operation.right = nums.pop()
                    operation.left = nums.pop()
                    nums.append(operation)
                ops.pop()
        while ops:
            op = ops.pop()
            op.right = nums.pop()
            op.left = nums.pop()
            nums.append(op)
        return nums[0] if nums else None
