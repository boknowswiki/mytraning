/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: A tree
 * @return: buttom-up level order a list of lists of integer
 */
func levelOrderBottom (root *TreeNode) [][]int {
    // write your code here
    if root == nil {
        return [][]int{}
    }
    
    q := []*TreeNode{root}
    var ret [][]int
    
    for len(q) != 0 {
        level := []*TreeNode{}
        var path []int
        for _, node := range q {
            path = append(path, node.Val)
            if node.Left != nil {
                level = append(level, node.Left)
            }
            if node.Right != nil {
                level = append(level, node.Right)
            }
        }
        q = level
        ret = append(ret, path)
    }
    
    ret = reverse(ret)
    
    return ret
}

func reverse(s [][]int) [][]int {
    //a := make([][]int, len(s))
    //copy(a, s)
    a := s

    for i := len(a)/2 - 1; i >= 0; i-- {
        opp := len(a) - 1 - i
        a[i], a[opp] = a[opp], a[i]
    }

    return a
}
