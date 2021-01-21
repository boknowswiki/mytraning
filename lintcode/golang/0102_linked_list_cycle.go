/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/**
 * @param head: The first node of linked list.
 * @return: True if it has a cycle, or false
 */
func hasCycle (head *ListNode) bool {
    // write your code here
    if head == nil || head.Next == nil {
        return false
    }
    
    fast := head.Next
    slow := head
    
    for fast != nil && fast.Next != nil {
        if fast == slow {
            return true
        }
        fast = fast.Next.Next
        slow = slow.Next
    }
    
    return false
}

