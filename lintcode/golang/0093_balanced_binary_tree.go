/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: The root of binary tree.
 * @return: True if this Binary tree is Balanced, or false.
 */
func isBalanced (root *TreeNode) bool {
    // write your code here
    if root == nil {
        return true
    }
    
    var helper func(*TreeNode) (bool, int)
    helper = func (node *TreeNode) (bool, int) {
        if node == nil {
            return true, 0
        }
        
        lb, l := helper(node.Left)
        if !lb {
            return false, 0
        }
        rb, r := helper(node.Right)
        if !rb {
            return false, 0
        }
        
        b := abs(l-r) <= 1
        return b, 1 + max(l, r)
    }
    
    rb, _ := helper(root)
    
    return rb
}

func max (a, b int) int {
    if a > b {
        return a
    }
    return b
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}
