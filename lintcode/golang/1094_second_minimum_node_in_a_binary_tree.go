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
 * @return: the second minimum value in the set made of all the nodes' value in the whole tree
 */
 
const MaxInt = int(^uint(0) >> 1)

func findSecondMinimumValue (root *TreeNode) int {
    // Write your code here
    if root == nil {
        return -1
    }
    
    var ret TreeNode
    ret.Val = MaxInt
    
    var helper func(*TreeNode)
    
    helper = func (node *TreeNode) {
        if node == nil {
            return
        }
        
        if (root.Val < node.Val) && (node.Val < ret.Val) {
            ret.Val = node.Val
        }
        
        helper(node.Left)
        helper(node.Right)
    }
    
    helper(root)
    
    if ret.Val != MaxInt {
        return ret.Val
    }
    
    return -1
}

