/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: param root: The root of the binary search tree
 * @param k1: An integer
 * @param k2: An integer
 * @return: return: Return all keys that k1<=key<=k2 in ascending order
 */
func searchRange (root *TreeNode, k1 int, k2 int) []int {
    // write your code here
    if root == nil {
        return []int{}
    }
    
    ret := []int{}
    var helper func (*TreeNode, int , int)
    
    helper = func (node *TreeNode, r1, r2 int) {
        if node == nil {
            return 
        }
        
        if node.Val > r1 {
            helper(node.Left, r1, r2)
        }
        
        if node.Val >= r1 && node.Val <= r2 {
            ret = append(ret, node.Val)
        }
        
        if node.Val < r2 {
            helper(node.Right, r1, r2)
        }
    }
    
    helper (root, k1, k2)
    
    return ret
}
