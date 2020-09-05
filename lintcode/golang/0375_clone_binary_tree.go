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
 * @return: root of new tree
 */
func cloneTree (root *TreeNode) *TreeNode {
    // write your code here
    if root == nil {
        return nil
    }
    
    node := &TreeNode {Val:root.Val}
    node.Left = cloneTree(root.Left)
    node.Right = cloneTree(root.Right)
    
    return node
}

