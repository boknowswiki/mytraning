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
 * @return: new root
 */
func upsideDownBinaryTree (root *TreeNode) *TreeNode {
    // write your code here
    if root == nil {
        return nil
    }
    
    if root.Left != nil {
        node := upsideDownBinaryTree(root.Left)
        root.Left.Right = root
        root.Left.Left = root.Right
        root.Left = nil
        root.Right = nil
        root = node
    }
    
    
    return root
}

