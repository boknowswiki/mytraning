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
func buildTree (inorder []int, postorder []int) *TreeNode {
    // write your code here
    n := len(postorder)
    if n == 0 || (n == 1 && postorder[0] == 0){
        return nil
    }
    
    val := postorder[n-1]
    root := TreeNode{Val: val}
    
    var index int
    
    for i, v := range inorder {
        if v == val {
            index = i
            break
        }
    }
    
    left := buildTree(inorder[:index], postorder[:index])
    right := buildTree(inorder[index+1:], postorder[index:n-1])
    
    root.Left = left
    root.Right = right
    
    return &root
}

