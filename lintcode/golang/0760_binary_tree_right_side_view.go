/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the root of the given tree
 * @return: the values of the nodes you can see ordered from top to bottom
 */
func rightSideView (root *TreeNode) []int {
    // write your code here
    ret := []int{}
    if root == nil {
        return ret
    }
    
    q := make([]*TreeNode, 0)
    q = append(q, root)
    
    for len(q) != 0 {
        level := make([]*TreeNode, 0)
        node := q[len(q)-1]
        ret = append(ret, node.Val)
        for _, n := range q {
            if n.Left != nil {
                level = append(level, n.Left)
            }
            if n.Right != nil {
                level = append(level, n.Right)
            }
        }
        q = level
    }
    
    return ret
}
