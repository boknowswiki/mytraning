/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: t
 * @return: the sum of all left leaves
 */
func sumOfLeftLeaves (root *TreeNode) int {
    // Write your code here
    if root == nil {
        return 0
    }
    
    var ret int
    
    var helper func (*TreeNode, bool)
    
    helper = func (node *TreeNode, isLeft bool) {
        if node == nil {
            return
        }
        
        if isLeft && node.Left == nil && node.Right == nil {
            ret += node.Val
            return
        }
        
        helper(node.Left, true)
        helper(node.Right, false)
        
        return
    }
    
    helper(root, false)
    
    return ret
}
