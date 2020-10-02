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
 * @return: the largest subtree's size which is a Binary Search Tree
 */
 
const MaxInt = int(^uint(0)>>1)
const MinInt = -MaxInt-1

func largestBSTSubtree (root *TreeNode) int {
    // Write your code here
    if root == nil {
        return 0
    }
    
    var helper func (*TreeNode) (int, int, int)
    
    helper = func (node *TreeNode) (m, n, v int) {
        if node == nil {
            return MaxInt, MinInt, 0
        }
        
        leftLow, leftHigh, leftNum := helper(node.Left)
        rightLow, rightHigh, rightNum := helper(node.Right)
        
        var nodeNum int
        nodeMin := MaxInt
        nodeMax := MinInt
        
        if leftHigh < node.Val && node.Val < rightLow {
            nodeNum = 1 + leftNum + rightNum
            nodeMin = min(node.Val, leftLow)
            nodeMax = max(node.Val, rightHigh)
        } else {
            nodeMin = MinInt
            nodeMax = MaxInt
            nodeNum = max(leftNum, rightNum)
        }
        
        return nodeMin, nodeMax, nodeNum
    }
    
    _, _, ret := helper(root)
    
    return ret
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
