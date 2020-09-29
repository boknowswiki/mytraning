

// bfs

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the given tree
 * @return: Whether it is a full tree
 */
func isFullTree (root *TreeNode) bool {
    // write your code here
    if root == nil {
        return true
    }
    
    q := make([]*TreeNode, 0)
    q = append(q, root)
    
    for len(q) != 0 {
        level := make([]*TreeNode, 0)
        for _, node := range q {
            if (node.Left == nil && node.Right != nil) || (node.Left != nil && node.Right == nil) {
                return false
            }
            if node.Left != nil {
                level = append(level, node.Left)
            }
            if node.Right != nil {
                level = append(level, node.Right)
            }
        }
        q = level
    }
    
    return true
}

// recursion


/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the given tree
 * @return: Whether it is a full tree
 */
func isFullTree (root *TreeNode) bool {
    // write your code here
    if root == nil {
        return true
    }
    
    if root.Left == nil && root.Right == nil {
        return true
    }
    
    if root.Left == nil || root.Right == nil {
        return false
    }
    
    return isFullTree(root.Left) && isFullTree(root.Right)
}

