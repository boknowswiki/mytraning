/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param a: the root of binary tree a.
 * @param b: the root of binary tree b.
 * @return: true if they are tweaked identical, or false.
 */
func isTweakedIdentical (a *TreeNode, b *TreeNode) bool {
    // write your code here
    if a == nil && b == nil {
        return true
    }
    if a != nil && b != nil && a.Val == b.Val {
        return (isTweakedIdentical(a.Left, b.Left) &&
            isTweakedIdentical(a.Right, b.Right)) ||
            (isTweakedIdentical(a.Left, b.Right) &&
            isTweakedIdentical(a.Right, b.Left))
           
    }
    
    return false
}

