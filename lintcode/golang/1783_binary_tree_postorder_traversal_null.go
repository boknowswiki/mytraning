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
 * @return: Postorder in ArrayList which contains node values.
 */
func postorderTraversal (root *TreeNode) []int {
    // write your code here
    if root == nil {
        return []int{}
    }
    
    var ret []int
    var helper func(*TreeNode, *[]int)
    helper = func(node *TreeNode, l *[]int) {
        if node == nil {
            return
        }
        helper(node.Left, l)
        helper(node.Right, l)
        *l = append(*l, node.Val)
        return
    }
    
    helper(root, &ret)
    
    return ret
}

