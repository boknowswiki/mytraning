#!/usr/bin/python -t

# hash table

# 面试官期望的解法：使用 Hash & Linked List 处理 Data Stream 的问题


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Solution:
    def __init__(self):
        self.d = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        
        for num in nums:
            if num not in self.d:
                node = Node(num)
                self.d[num] = node
                self.add_to_end(node)
            else:
                if self.d[num] != None:
                    node = self.d[num]
                    self.remove(node)
                    self.d[num] = None
                    
            if num == number:
                return self.head.next.val
                
        return -1
        
    def add_to_end(self, node):
        prev = self.tail.prev
        next = self.tail
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node
        
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        
        
