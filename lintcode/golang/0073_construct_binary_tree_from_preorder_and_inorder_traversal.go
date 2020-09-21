/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param inorder: A list of integers that inorder traversal of a tree
 * @param postorder: A list of integers that postorder traversal of a tree
 * @return: Root of a tree
 */
func buildTree (preorder []int, inorder []int) *TreeNode {
    // write your code here
    n := len(preorder)
    if n == 0 || (n == 1 && preorder[0] == 0) {
        return nil
    }
    
    val := preorder[0]
    root := TreeNode { Val: val}
    var index int
    
    for i, v := range inorder {
        if v == val {
            index = i
            break
        }
    }
    
    left := buildTree(preorder[1:index+1], inorder[:index])
    right := buildTree(preorder[index+1:], inorder[index+1:])
    
    root.Left = left
    root.Right = right
    
    return &root
}
