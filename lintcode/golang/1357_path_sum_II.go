/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: a binary tree
 * @param sum: the sum
 * @return: the scheme
 */
func pathSum (root *TreeNode, sum int) [][]int {
    // Write your code here.
    if root == nil {
        return [][]int{}
    }
    
    var ret [][]int
    var dfs func(*TreeNode, int, []int)
    
    dfs = func(node *TreeNode, target int, path []int) {
        if node == nil {
            return
        }
        if node.Left == nil && node.Right == nil && target == node.Val {
            path = append(path, node.Val)
            ret = append(ret, append([]int{}, path...))
            return
        }
        
        path = append(path, node.Val)
        dfs(node.Left, target-node.Val, path)
        dfs(node.Right, target-node.Val, path)
        path = path[:len(path)-1]
    }
    
    dfs(root, sum, []int{})
    
    return ret
}

