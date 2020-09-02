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
func maxDepth (root *TreeNode) int {
    // write your code here
    ret := 0
    if root == nil {
        return ret
    }
    
    q := make([]*TreeNode, 0)
    q = append(q, root)
    ret++
    
    for len(q) != 0 {
        level := make([]*TreeNode, 0)
        for _, node := range q {
            if node.Left != nil {
                level = append(level, node.Left)
            }
            if node.Right != nil {
                level = append(level, node.Right)
            }
        }
        q = level
        if len(level) != 0 {
            ret++
        }
    }
    
    return ret
}

