/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: given BST
 * @param minimum: the lower limit
 * @param maximum: the upper limit
 * @return: the root of the new tree 
 */
func trimBST (root *TreeNode, minimum int, maximum int) *TreeNode {
    // write your code here
    if root == nil {
        return nil
    }
    
    if root.Val < minimum {
        return trimBST(root.Right, minimum, maximum)
    } else if root.Val > maximum {
        return trimBST(root.Left, minimum, maximum)
    } else {
        root.Left = trimBST(root.Left, minimum, maximum)
        root.Right = trimBST(root.Right, minimum, maximum)
    }
    
    return root
}

