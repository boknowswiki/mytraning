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
 * @return: An integer
 */
const MaxUint = ^uint(0) 
const MinUint = 0 
const MaxInt = int(MaxUint >> 1) 
const MinInt = -100000
func maxPathSum (root *TreeNode) int {
    // write your code here
    if root == nil {
        return 0
    }
    
    var helper func (*TreeNode) (int, int)
    helper = func(node *TreeNode) (int, int) {
        if node == nil {
            return MinInt, MinInt
        }
        
        lMax, left := helper(node.Left)
        rMax, right := helper(node.Right)
        
        retMax := max(max(max(lMax, left+node.Val), max(rMax, right+node.Val)), left+node.Val+right)
        retMax = max(retMax, node.Val)
        single := max(left+node.Val, right+node.Val)
        single = max(single, node.Val)
        
        return retMax, single
    }
    
    maxVal, _ := helper(root)
    
    return maxVal
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
