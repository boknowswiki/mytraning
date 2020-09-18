/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root1: the first tree
 * @param root2: the second tree
 * @return: returns whether the leaf sequence is the same
 */
func leafSimilar (root1 *TreeNode, root2 *TreeNode) bool {
    // write your code here.
    l1 := make([]int, 0)
    l2 := make([]int, 0)
    
    var helper func (node *TreeNode, l *[]int)
    helper = func (node *TreeNode, l *[]int) {
        if node == nil {
            return
        }
        
        if node.Left == nil && node.Right == nil {
            *l = append(*l, node.Val)
        }
        if node.Left != nil {
            helper(node.Left, l)
        }
        if node.Right != nil {
            helper(node.Right, l)
        }
    }
    
    helper(root1, &l1)
    helper(root2, &l2)
    
    if len(l1) != len(l2) {
        return false
    }
    
    for i, v := range l1 {
        if v != l2[i] {
            return false
        }
    }
    
    return true
}

