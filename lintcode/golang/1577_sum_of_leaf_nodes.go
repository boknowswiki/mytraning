


/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: 
 * @return: the sum of leafnode
 */
func sumLeafNode (root *TreeNode) int {
    // Write your code here
    if root == nil {
        return 0
    }
    
    if root.Left == nil && root.Right == nil {
        return root.Val
    }
    
    left := sumLeafNode(root.Left)
    right:= sumLeafNode(root.Right)
    
    return left+right
}

