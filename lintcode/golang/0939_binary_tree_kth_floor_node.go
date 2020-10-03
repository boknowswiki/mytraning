/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the root node
 * @param k: an integer
 * @return: the number of nodes in the k-th layer of the binary tree
 */
func kthfloorNode (root *TreeNode, k int) int {
    // Write your code here
    if root == nil {
        return 0
    }
    
    q := make([]*TreeNode, 0)
    var ret int
    q = append(q, root)
    
    for len(q) != 0 {
        ret = len(q)
        level := make([]*TreeNode, 0)
        
        if k == 1 {
            return ret
        }
        for _, node := range q {
            if node.Left != nil {
                level = append(level, node.Left)
            }
            if node.Right != nil {
                level = append(level, node.Right)
            }
        }
        
        q = level
        k--
    }
    
    return 0
}
