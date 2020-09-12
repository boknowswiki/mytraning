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
 * @return: the new root
 */

var val int 

func convertBST (root *TreeNode) *TreeNode {
    // write your code here
    dfs(root)
    return root
}

func dfs (node *TreeNode) {
    if node == nil {
        return
    }
    
    dfs(node.Right)
    val += node.Val
    node.Val = val
    dfs(node.Left)
    
    return
}
