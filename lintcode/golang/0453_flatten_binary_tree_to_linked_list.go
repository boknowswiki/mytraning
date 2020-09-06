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
func flatten (root **TreeNode)  {
    // write your code here
    if *root == nil {
        return
    }
    
    _ = helper((*root))

    return
}

func helper(node *TreeNode) *TreeNode {
    if node == nil {
        return nil
    }
    
    leftLast := helper(node.Left)
    rightLast := helper(node.Right)
    
    if leftLast != nil {
        leftLast.Right = node.Right
        node.Right = node.Left
        node.Left = nil

    }
    
    if rightLast != nil {
        return rightLast
    }
    if leftLast != nil {
        return leftLast
    }
    
    return node
}
