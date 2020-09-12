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
 * @return: the root of the maximum average of subtree
 */

const MaxUint = ^uint(0)
const MinUint = 0

const MaxInt = int(^uint(0) >> 1)
const MinInt = -MaxInt - 1

func findSubtree2 (root *TreeNode) *TreeNode {
    // write your code here
    if root == nil {
        return nil
    }

    var ret *TreeNode
    ret = nil
    avg := MinInt
    
    helper(root, &avg, &ret)
    
    return ret
}

func helper (node *TreeNode, avg *int, ret **TreeNode) (int, int) {
    if node == nil {
        return 0, 0
    }
    
    leftTotal, leftNum := helper(node.Left, avg, ret)
    rightTotal, rightNum := helper(node.Right, avg, ret)
    
    nodeTotal := (leftTotal + node.Val + rightTotal)/(leftNum+1+rightNum)
    
    if *ret == nil || (nodeTotal/(leftNum+1+rightNum)) > *avg {
        *avg = nodeTotal
        *ret = node
    }
    
    return nodeTotal, (leftNum+1+rightNum)
}
