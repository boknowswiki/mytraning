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
 * @return: True if the binary tree is BST, or false
 */
func isValidBST (root *TreeNode) bool {
    // write your code here
    if root == nil {
        return true
    }
    
    //if (root.Left == nil && root.Right != nil) || (root.Left != nil && root.Right == nil) {
    //    return false
    //}
    
    var left func (*TreeNode, *TreeNode) bool
    var right func (*TreeNode, *TreeNode) bool
    
    left = func (p *TreeNode, n *TreeNode) bool {
        if n == nil {
            return true
        }
        if n.Val >= p.Val {
            return false
        }
        if (n.Left != nil && (n.Left.Val >= n.Val || n.Left.Val >= p.Val)) || (n.Right != nil && (n.Right.Val <= n.Val || n.Right.Val >= p.Val)) {
            return false
        }
        
        return left(n, n.Left) && right(n, n.Right)
    }
    
    right = func (p *TreeNode, n *TreeNode) bool {
        if n == nil {
            return true
        }
        
        if n.Val <= p.Val {
            return false
        }
        
        if (n.Left != nil && (n.Left.Val >= n.Val || n.Left.Val <= p.Val)) || (n.Right != nil && (n.Right.Val <= n.Val || n.Right.Val <= p.Val)) {
            return false
        }
        
        return left(n, n.Left) && right(n, n.Right)
    }
    
    return left(root, root.Left) && right(root, root.Right)
}

