/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the root of binary tree
 * @return: the length of the longest consecutive sequence path
 */
func longestConsecutive2 (root *TreeNode) int {
    // write your code here
    if root == nil {
        return 0
    }
    
    ret, _, _ := helper(root)
    
    return ret
}

func helper(node *TreeNode) (int, int, int) {
    if node == nil {
        return 0, 0, 0
    }
    
    left_ret, left_up, left_down := helper(node.Left)
    right_ret, right_up, right_down := helper(node.Right)
    
    up, down := 0, 0
    
    if node.Left != nil {
        if node.Left.Val == node.Val + 1 {
            up = max(left_up+1, up)
        }
        if node.Left.Val + 1 == node.Val {
            down = max(left_down+1, down)
        }
    }
    
    if node.Right != nil {
        if node.Right.Val == node.Val + 1 {
            up = max(right_up+1, up)
        }
        if node.Right.Val + 1 == node.Val {
            down = max(right_down+1, down)
        }
    }
    
    ret := up + 1 + down
    ret = max(max(left_ret, right_ret), ret)
    
    return ret, up, down
}

func max(a, b int) int {
    if a > b {
        return a
    }
    
    return b
}
