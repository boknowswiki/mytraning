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
 * @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
 */
func zigzagLevelOrder (root *TreeNode) [][]int {
    // write your code here
    if root == nil {
        return [][]int{}
    }
    
    q := []*TreeNode{root}
    ret := [][]int{}
    needReverse := false
    
    for len(q) != 0 {
        level := []*TreeNode{}
        path := []int{}
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
        if needReverse {
            reverse(path)
        }
        ret = append(ret, path)
        needReverse = !needReverse
    }
    
    return ret
}

func reverse (path []int) {
    l := 0
    r := len(path)-1
    
    for l < r {
        tmp := path[l]
        path[l] = path[r]
        path[r] = tmp
        l++
        r--
    }
    
    return
}
