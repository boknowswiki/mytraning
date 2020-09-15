/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the root
 * @return: the minimum difference between the values of any two different nodes in the tree
 */
 
//import "fmt"

const MaxInt = int(^uint(0)>>1)

func minDiffInBST (root *TreeNode) int {
    // Write your code here
    var q []*TreeNode
    
    dfs(root, &q)
    
    //fmt.Println(q)
    
    ret := MaxInt
    
    for i := 1; i < len(q); i++ {
        ret = min(ret, (q[i].Val - q[i-1].Val))
        //fmt.Println(q[i].Val)
    }
    
    return ret
}

func dfs(node *TreeNode, q *[]*TreeNode) {
    if node == nil {
        return
    }
    
    dfs(node.Left, q)
    *q = append(*q, node)
    dfs(node.Right, q)
    return
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
