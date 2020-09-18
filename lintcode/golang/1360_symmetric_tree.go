/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: root of the given tree
 * @return: whether it is a mirror of itself 
 */
func isSymmetric (root *TreeNode) bool {
    // Write your code here
    if root == nil {
        return true
    }
    
    var helper func (*TreeNode, *TreeNode) bool
    
    helper = func (left *TreeNode, right *TreeNode) bool {
        if left == nil || right == nil {
            return left == right
        }
        
        if left.Val != right.Val {
            return false
        }
        
        return helper(left.Left, right.Right) && helper(left.Right, right.Left)
    }
    
    return helper(root.Left, root.Right)
}

