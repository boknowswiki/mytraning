package main

// dp  && dfs
// time O(n) because traveral the tree once, space O(n) because n nodes.

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * @param root: The root of binary tree.
 * @return: The maximum amount of money you can rob tonight
 */
func houseRobber3(root *TreeNode) int {
	// write your code here
	rob, notRob := dfs(root)

	return max(rob, notRob)
}

func dfs(node *TreeNode) (int, int) {
	if node == nil {
		return 0, 0
	}

	leftRob, leftNotRob := dfs(node.Left)
	rightRob, rightNotRob := dfs(node.Right)

	rob := node.Val + leftNotRob + rightNotRob
	notRob := max(leftRob, leftNotRob) + max(rightRob, rightNotRob)

	return rob, notRob
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	a := &TreeNode{Val: 3}
	fmt.Println(houseRobber3(a))
}
