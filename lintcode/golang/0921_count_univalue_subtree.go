/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the given tree
 * @return: the number of uni-value subtrees.
 */
func countUnivalSubtrees (root *TreeNode) int {
    // write your code here
    if root == nil {
        return 0
    }
    
    var cnt int
    
    var helper func(*TreeNode) bool
    
    helper = func (node *TreeNode) bool {
        if node == nil {
            return true
        }
        
        left := helper(node.Left)
        right := helper(node.Right)
        
        if left && right && 
        (node.Left == nil || (node.Left.Val == node.Val)) &&
        (node.Right == nil || (node.Right.Val == node.Val)) {
                cnt++
                return true
        }
        return false
    }
    
    helper(root)
    
    return cnt
}
