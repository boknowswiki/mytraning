#!/usr/bin/python -t

# hash table

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        hashsize = 2 * len(hashTable)
        newhash = [None] * hashsize
        for key in hashTable:
            item = key
            
            while item != None:
                self.addNode(newhash, item.val)
                item = item.next
                
        return newhash
        
    def addNode(self, newhash, val):
        key = val % len(newhash)
        if newhash[key] == None:
            newhash[key] = ListNode(val)
        else:
            self.addNodeToList(newhash[key], val)
            
    def addNodeToList(self, node, val):
        new_node = ListNode(val)
        while node.next:
            node = node.next
            
        node.next = new_node
        
        return
    
