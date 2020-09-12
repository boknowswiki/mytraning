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
 * @return: the maximum weight node
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
    
    var ret TreeNode
    retNodeP := &ret
    maxVal := MinInt
    
    helper(root, &maxVal, &retNodeP)
    
    return retNodeP
}

func helper(node *TreeNode, maxVal *int, ret **TreeNode) int {
    if node == nil {
        return 0
    }
    
    left := helper(node.Left, maxVal, ret)
    right := helper(node.Right, maxVal, ret)
    
    nodeVal := left+right+node.Val
    
    if *ret == nil || nodeVal > *maxVal {
        *maxVal = node.Val
        *ret = node
    }
    
    return nodeVal
}
