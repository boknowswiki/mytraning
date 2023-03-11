#!/usr/bin/python -t

# binary tree and linked list
# time O(n)
# space O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Form an array out of the given linked list and then
        # use the array to form the BST.
        values = self.mapListToValues(head)

        # l and r represent the start and end of the given array
        def convertListToBST(l, r):

            # Invalid case
            if l > r:
                return None

            # Middle element forms the root.
            mid = (l + r) // 2
            node = TreeNode(values[mid])

            # Base case for when there is only one element left in the array
            if l == r:
                return node

            # Recursively form BST on the two halves
            node.left = convertListToBST(l, mid - 1)
            node.right = convertListToBST(mid + 1, r)
            return node
        return convertListToBST(0, len(values) - 1)


    # Convert the given linked list to an array
    def mapListToValues(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals  

# binary tree and linked list
# time O(nlogn)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.helper(head)
    
    def helper(self, node):
        if not node:
            return None
        if not node.next:
            return TreeNode(node.val)
        
        slow, fast = node, node.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        root_node = slow.next
        slow.next = None
        root = TreeNode(val=root_node.val)
        root.left = self.helper(node)
        root.right = self.helper(root_node.next)
        
        return root

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedlisttobst(self, start, end):
        if start > end:
            return None
        mid = (start + end) /2
        left = self.sortedlisttobst(start, mid-1)
        p = TreeNode(self.head.val)
        p.left = left
        self.head = self.head.next
        p.right = self.sortedlisttobst(mid+1, end)

        return p
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        

        self.head = head
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n = n + 1

        return self.sortedlisttobst(0, n-1)

    
    public TreeNode sortedListToBST(ListNode head) {
    if(head == null)
        return null;
    ListNode fast = head;
    ListNode slow = head;
    ListNode prev =null; 
    while(fast != null && fast.next != null)
    {
        fast = fast.next.next;
        prev =slow;
        slow=slow.next;
    }
    TreeNode root = new TreeNode(slow.val);
    if(prev != null)
        prev.next = null;
    else
        head  = null;
        
    root.left = sortedListToBST(head);
    root.right = sortedListToBST(slow.next);
    return root;
}
