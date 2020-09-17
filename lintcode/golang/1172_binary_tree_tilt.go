/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the root
 * @return: the tilt of the whole tree
 */
func findTilt (root *TreeNode) int {
    // Write your code here
    if root == nil {
        return 0
    }
    
    var ret int
    
    var helper func (*TreeNode) int
    helper = func (node *TreeNode) int {
        if node == nil {
            return 0
        }
        
        left := helper(node.Left)
        right := helper(node.Right)
        
        ret += abs(left-right)
        
        return left + right + node.Val
    }
    
    helper(root)
    
    return ret
}

func abs (a int) int {
    if a < 0 {
        return -a
    }
    return a
}
