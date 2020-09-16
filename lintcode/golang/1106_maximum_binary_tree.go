/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param nums: an array
 * @return: the maximum tree
 */
 
const MaxInt = int(^uint(0) >> 1)
const MinInt = -MaxInt-1

func constructMaximumBinaryTree (nums []int) *TreeNode {
    // Write your code here
    if len(nums) == 0 {
        return nil
    }
    if len(nums) == 1 {
        return &TreeNode {
            Val: nums[0],
        }
    }
    
    maxVal := MinInt
    maxIndex := 0
    
    for index, val := range nums {
        if val > maxVal {
            maxVal = val
            maxIndex = index
        }
    }
    
    node := &TreeNode {
        Val: nums[maxIndex],
    }
    
    node.Left = constructMaximumBinaryTree(nums[:maxIndex])
    node.Right = constructMaximumBinaryTree(nums[maxIndex+1:len(nums)])
    
    return node
}

