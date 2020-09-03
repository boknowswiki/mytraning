// iterative way

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: a TreeNode, the root of the binary tree
 * @return: nothing
 */
func invertBinaryTree (root **TreeNode)  {
    // write your code here
    if *root == nil {
        return
    }
    
    q := make([]*TreeNode, 0)
    q = append(q, *root)
    
    for len(q) != 0 {
        level := make([]*TreeNode, 0)
        for _, node := range q {
            tmp := node.Left
            node.Left = node.Right
            node.Right = tmp
            if node.Left != nil {
                level = append(level, node.Left)
            }
            if node.Right != nil {
                level = append(level, node.Right)
            }
        }
        q = level
    }
    
    return
}



// recursive way

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: a TreeNode, the root of the binary tree
 * @return: nothing
 */
func invertBinaryTree (root **TreeNode)  {
    // write your code here
    if *root == nil {
        return
    }
    
    var helper func(node *TreeNode) *TreeNode
    
    helper = func (node *TreeNode) *TreeNode {
        if node == nil {
            return nil
        }
        if node.Left == nil && node.Right == nil {
            return node
        }
        left := helper(node.Left)
        right := helper(node.Right)
        node.Left = right
        node.Right = left
        
        return node
    }
    helper(*root)
    
    return
}

