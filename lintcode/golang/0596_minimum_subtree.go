/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the root of binary tree
 * @return: the root of the minimum subtree
 */
 
const MaxUint = ^uint(0)
const MinUint = 0

const MaxInt = int(^uint(0) >> 1)
const MinInt = -MaxInt - 1

func findSubtree (root *TreeNode) *TreeNode {
    // write your code here
    if root == nil {
        return nil
    }
    
    minVal := MaxInt
    ret := root
    _ = helper(root, &minVal, &ret)
    
    return ret
}

func helper(node *TreeNode, minVal *int, ret **TreeNode) int {
    if node == nil {
        return 0
    }

    left := helper(node.Left, minVal, ret)
    right := helper(node.Right, minVal, ret)
    
    val := node.Val + left + right
    
    if val < *minVal {
        *minVal = val
        *ret = node
    }
    
    return val
}
