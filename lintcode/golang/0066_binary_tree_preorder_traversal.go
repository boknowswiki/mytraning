
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: A Tree
 * @return: Preorder in ArrayList which contains node values.
 */
func preorderTraversal (root *TreeNode) []int {
    // write your code here
    ret := make([]int, 0)
    
    helper(root, &ret)
    
    return ret
}

func helper(node *TreeNode, ret *[]int) {
    if node != nil {
        *ret = append(*ret, node.Val)
        
        if node.Left != nil {
            helper(node.Left, ret)
        }
        if node.Right != nil {
            helper(node.Right, ret)
        }
    }
}
