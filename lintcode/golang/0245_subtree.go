/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param T1: The roots of binary tree T1.
 * @param T2: The roots of binary tree T2.
 * @return: True if T2 is a subtree of T1, or false.
 */
func isSubtree (T1 *TreeNode, T2 *TreeNode) bool {
    // write your code here
    if T2 == nil {
        return true
    }
    
    if T1 == nil {
        return false
    }
    
    if isEqual(T1, T2) {
        return true
    }
    
    return isSubtree(T1.Left, T2) || isSubtree(T1.Right, T2)
}

func isEqual(t1, t2 *TreeNode) bool {
    if t1 == nil && t2 == nil {
        return true
    }
    
    if t1 == nil || t2 == nil {
        return false
    }
    if t1.Val != t2.Val {
        return false
    }
    return isEqual(t1.Left, t2.Left) && isEqual(t1.Right, t2.Right)
}
