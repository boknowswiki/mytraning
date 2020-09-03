/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: The root of binary tree
 * @return: An integer
 */
func minDepth (root *TreeNode) int {
    // write your code here
    var ret int
    
    if root == nil {
        return ret
    }
    
    q := make([]*TreeNode, 0)
    q = append(q, root)
    ret++
    
    for len(q) != 0 {
        level := make([]*TreeNode, 0)
        for _, node := range q {
            if node.Left == nil && node.Right == nil {
                return ret
            }
            if node.Left != nil {
                level = append(level, node.Left)
            }
            if node.Right != nil {
                level = append(level, node.Right)
            }
        }
        ret++
        q = level
    }
    
    return ret
}

