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
 * @return: the length of the longest consecutive sequence path
 */

import "fmt"

func longestConsecutive (root *TreeNode) int {
    // write your code here
    if root == nil {
        return 0
    }
    
    var ret int
    _ = helper(root, &ret)
    
    return ret
}

func helper(root *TreeNode, maxVal *int) int {
    if root == nil {
        return 0
    }
    
    if root.Left == nil && root.Right == nil {
        return 1
    }
    
    left := helper(root.Left, maxVal)
    right := helper(root.Right, maxVal)
    
    fmt.Println(root.Val, left, right)
    var ret int
    ret = max(left, right)
    if root.Left != nil && root.Val + 1 == root.Left.Val {
        fmt.Println("left", root.Left.Val, root.Val, left, ret)
        ret = max(ret, left+1)
    } else {
        left = 0   
    }
    
    if root.Right != nil && root.Val +1 == root.Right.Val {
        fmt.Println("right", root.Right.Val, root.Val, right, ret)
        ret = max(ret, right+1)
    } else {
        right = 0
    }
    
    *maxVal = max(*maxVal, ret)
    if left == 0 && right == 0 {
        ret = 1
    }
    
    return ret
}

func max (a, b int) int {
    if a > b {
        return a
    }
    return b
}
