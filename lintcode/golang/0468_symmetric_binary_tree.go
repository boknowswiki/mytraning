/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the root of binary tree.
 * @return: true if it is a mirror of itself, or false.
 */
func isSymmetric (root *TreeNode) bool {
    // write your code here
    if root == nil {
        return true
    }
    
    return helper(root.Left, root.Right)
}

func helper (a, b *TreeNode) bool {
    if a == nil && b == nil {
        return true
    }
    if a != nil && b != nil && a.Val == b.Val {
        return helper(a.Left, b.Right) && helper(a.Right, b.Left)
    }
    
    return false
}
