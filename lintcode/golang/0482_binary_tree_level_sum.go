/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the root of the binary tree
 * @param level: the depth of the target level
 * @return: An integer
 */
func levelSum (root *TreeNode, level int) int {
    // write your code here
    if root == nil {
        return 0
    }
    
    q := make([]*TreeNode, 0)
    var total int
    q = append(q, root)
    
    for len(q) > 0 {
        l := make([]*TreeNode, 0)

        if level == 0 {
            return total
        }
        
        total = 0
        level--
        
        for _, node := range q {
            total += node.Val
            if node.Left != nil {
                l = append(l, node.Left)
            }
            if node.Right != nil {
                l = append(l, node.Right)
            }
        }
        
        q = l
    }
    
    if level != 0 {
        return 0
    }
    
    return total
}
