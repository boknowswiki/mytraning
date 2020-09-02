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
 * @return: Level order a list of lists of integer
 */
func levelOrder (root *TreeNode) [][]int {
    // write your code here
    ret := make([][]int, 0)
    if root == nil {
        return ret
    }
    
    q := make([]*TreeNode, 0)
    q = append(q, root)
    
    for len(q) != 0 {
        level := make([]*TreeNode, 0)
        tmp := make([]int, 0)
        for _, node := range q {
            tmp = append(tmp, node.Val)
            if node.Left != nil {
                level = append(level, node.Left)
            }
            if node.Right != nil {
                level = append(level, node.Right)
            }
        }
        q = level
        ret = append(ret, tmp)
    }
    
    return ret
}

